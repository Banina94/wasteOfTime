# sudoku_generator.py
import random

class SudokuGenerator:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.solutions_count = 0
        self.solved_grid_result = None # To store the first found solution

    def solve_sudoku(self, grid_to_solve):
        """Solves a Sudoku puzzle and counts solutions.
        Returns the first found solution grid if unique, otherwise None."""
        self.solutions_count = 0 # Reset for each solve call
        self.solved_grid_result = None
        temp_grid = [row[:] for row in grid_to_solve] # Work on a copy

        self._solve_recursive(temp_grid)

        if self.solutions_count == 1:
            return self.solved_grid_result # Return the stored unique solution
        return None # No unique solution or multiple solutions

    def _solve_recursive(self, grid_to_solve):
        # Optimization: if more than one solution found, no need to continue
        if self.solutions_count > 1:
            return

        r, c = self._find_empty(grid_to_solve)
        if r is None: # Grid is filled
            self.solutions_count += 1
            if self.solutions_count == 1: # Store the first unique solution found
                self.solved_grid_result = [row[:] for row in grid_to_solve]
            return

        for num in range(1, 10):
            if self._is_valid(grid_to_solve, r, c, num):
                grid_to_solve[r][c] = num
                self._solve_recursive(grid_to_solve)
                grid_to_solve[r][c] = 0  # Backtrack

    def _find_empty(self, grid):
        """Finds an empty cell (0) in the grid."""
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0:
                    return r, c
        return None, None

    def _is_valid(self, grid, r, c, num):
        """Checks if a number can be placed in a given cell."""
        # Check row
        for x in range(9):
            if grid[r][x] == num:
                return False

        # Check column
        for x in range(9):
            if grid[x][c] == num:
                return False

        # Check 3x3 box
        start_row = r - r % 3
        start_col = c - c % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def _fill_grid(self, grid):
        """Recursively fills the grid to create a complete Sudoku solution."""
        r, c = self._find_empty(grid)
        if r is None:
            return True  # Grid is filled

        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if self._is_valid(grid, r, c, num):
                grid[r][c] = num
                if self._fill_grid(grid):
                    return True
                grid[r][c] = 0  # Backtrack
        return False

    def generate_full_solution(self):
        """Generates a complete, valid Sudoku solution."""
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self._fill_grid(self.grid)
        return [row[:] for row in self.grid] # Return a copy

    def generate_puzzle(self, num_missing_cells):
        """
        Generates a Sudoku puzzle with a specific number of missing cells,
        ensuring the puzzle has a unique solution.
        """
        full_solution = self.generate_full_solution()
        puzzle = [row[:] for row in full_solution] # Start with a copy of the full solution

        cells_to_remove = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells_to_remove)

        current_missing_count = 0
        # original_values = {} # Not strictly needed if we restore immediately

        for r, c in cells_to_remove:
            if current_missing_count >= num_missing_cells:
                break # Reached the target number of missing cells

            original_value = puzzle[r][c] # Store original value
            puzzle[r][c] = 0 # Temporarily remove

            # Check if the puzzle still has a unique solution
            temp_solver = SudokuGenerator() # Use a temporary solver instance
            temp_solver.solve_sudoku([row[:] for row in puzzle]) # Pass a copy

            if temp_solver.solutions_count == 1:
                current_missing_count += 1
            else:
                # If removing it leads to non-unique solution, restore the value
                puzzle[r][c] = original_value

        return puzzle, full_solution

    def classify_difficulty(self, puzzle):
        """
        Classifies difficulty based on the number of clues (81 - missing cells).
        This is now directly tied to the generation parameters.
        """
        clues = sum(1 for row in puzzle for cell in row if cell != 0)
        missing_cells = 81 - clues

        if missing_cells <= 45:
            return "Easy"
        elif missing_cells <= 55:
            return "Medium"
        else:
            return "Hard"


def _print_grid(grid):
    for r, row in enumerate(grid):
        line = ''
        for c, n in enumerate(row):
            char = str(n) if n != 0 else '.'
            line += char + (' ' if c % 3 != 2 else '  ')
        print(line)
        if r % 3 == 2 and r != 8:
            print()


if __name__ == '__main__':
    sg = SudokuGenerator()
    
    # Ask user for difficulty level
    print("=" * 50)
    print("Welcome to Sudoku Generator!")
    print("=" * 50)
    print("\nSelect difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print()
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            difficulty = 'Easy'
            missing = 35  # Easy: fewer missing cells (more clues)
            break
        elif choice == '2':
            difficulty = 'Medium'
            missing = 50  # Medium: moderate missing cells
            break
        elif choice == '3':
            difficulty = 'Hard'
            missing = 60  # Hard: more missing cells (fewer clues)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    print(f"\nGenerating {difficulty} puzzle...\n")
    puzzle, solution = sg.generate_puzzle(missing)

    print(f"Generated puzzle (missing {missing} cells)\n")
    print("PUZZLE:")
    print("-" * 30)
    _print_grid(puzzle)

    print("\n" + "=" * 50)
    print("SOLUTION:")
    print("=" * 50)
    _print_grid(solution)