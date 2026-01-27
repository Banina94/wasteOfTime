import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.crossword.variables:
            # Remove all words that don't match the variable's length
            to_remove = set()
            for word in self.domains[var]:
                if len(word) != var.length:
                    to_remove.add(word)
            for word in to_remove:
                self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        overlap = self.crossword.overlaps[x, y]

        # If there's no overlap, x and y are already consistent
        if overlap is None:
            return False

        i, j = overlap  # i is the index in x's word, j is the index in y's word

        # Check each value in x's domain
        to_remove = set()
        for word_x in self.domains[x]:
            # Check if there's a word in y's domain that doesn't conflict
            has_compatible = False
            for word_y in self.domains[y]:
                if word_x[i] == word_y[j]:
                    has_compatible = True
                    break

            # If no compatible word found, remove this value from x's domain
            if not has_compatible:
                to_remove.add(word_x)
                revised = True

        for word in to_remove:
            self.domains[x].remove(word)

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Initialize queue with all arcs if not provided
        if arcs is None:
            queue = []
            for x in self.crossword.variables:
                for y in self.crossword.variables:
                    if x != y:
                        queue.append((x, y))
        else:
            queue = list(arcs)

        # Process arcs
        while queue:
            x, y = queue.pop(0)

            if self.revise(x, y):
                # If x's domain is now empty, no solution exists
                if len(self.domains[x]) == 0:
                    return False

                # Add all neighbors of x (except y) to the queue
                for z in self.crossword.neighbors(x):
                    if z != y:
                        queue.append((z, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        return len(assignment) == len(self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Check that all values are unique
        values = list(assignment.values())
        if len(values) != len(set(values)):
            return False

        # Check that each value is the correct length
        for var, word in assignment.items():
            if len(word) != var.length:
                return False

        # Check that there are no conflicts between neighbors
        for var, word in assignment.items():
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    # Get the overlap information
                    overlap = self.crossword.overlaps[var, neighbor]
                    i, j = overlap  # i is index in var's word, j is index in neighbor's word

                    if word[i] != assignment[neighbor][j]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        def heuristic(word):
            """Count how many values are ruled out for neighboring variables."""
            ruled_out = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:
                    overlap = self.crossword.overlaps[var, neighbor]
                    if overlap is not None:
                        i, j = overlap
                        for neighbor_word in self.domains[neighbor]:
                            if neighbor_word[j] != word[i]:
                                ruled_out += 1
            return ruled_out

        # Return domain values sorted by number of ruled out values (ascending)
        return sorted(self.domains[var], key=heuristic)

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Get unassigned variables
        unassigned = [var for var in self.crossword.variables if var not in assignment]

        # Sort by: 1) fewest remaining values (MRV), 2) most neighbors (degree)
        return min(unassigned, key=lambda var: (len(self.domains[var]), -len(self.crossword.neighbors(var))))

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Base case: if assignment is complete, we found a solution
        if self.assignment_complete(assignment):
            return assignment

        # Choose an unassigned variable
        var = self.select_unassigned_variable(assignment)

        # Try each value in the domain of the selected variable
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value

            # Check if the new assignment is consistent
            if self.consistent(new_assignment):
                # Save the current domains in case we need to backtrack
                old_domains = {v: self.domains[v].copy() for v in self.crossword.variables}

                # Add variable to assignment
                self.domains[var] = {value}

                # Enforce arc consistency on affected variables
                arcs_to_check = [(neighbor, var) for neighbor in self.crossword.neighbors(var)]
                if self.ac3(arcs_to_check):
                    # Recursively try to complete the assignment
                    result = self.backtrack(new_assignment)
                    if result is not None:
                        return result

                # Restore domains if backtracking
                self.domains = old_domains

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
