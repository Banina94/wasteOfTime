import random
import string

class LatinWordSearch:
    """Generate a word search puzzle with 100 Latin words."""
    
    # 100 Latin words (common vocabulary)
    LATIN_WORDS = [
        'AMICUS', 'AMICA', 'AMOR', 'ANIMUS', 'ANIMAL', 'ANNUS', 'AQUA', 'ARBOR', 'ARCUS', 'ARS',
        'ARMA', 'AURUM', 'AUTO', 'AVIS', 'AXIS', 'BAMBAM', 'BESTIA', 'BIBLIA', 'BILIS', 'BONUM',
        'BONUS', 'BOTANUS', 'BRACHIUM', 'BREVITAS', 'CABALLUS', 'CABANA', 'CACUS', 'CAECA', 'CAEDIS', 'CAELUM',
        'CAENATIO', 'CAERULEUS', 'CAESURA', 'CAFEA', 'CAIFAS', 'CAIETA', 'CAIUS', 'CALAMITAS', 'CALAMUS', 'CALANTICA',
        'CALCANEUS', 'CALCAR', 'CALCATOR', 'CALCEUS', 'CALCULATUS', 'CALDARIA', 'CALDUS', 'CALEA', 'CALENDAE', 'CALENDA',
        'CALENTURA', 'CALEPO', 'CALESCO', 'CALETA', 'CALFATER', 'CALIBER', 'CALIDARIUM', 'CALIDITAS', 'CALIDUS', 'CALIGA',
        'CALIGATIO', 'CALIGATOR', 'CALIGATUS', 'CALIGULA', 'CALIGO', 'CALIGINOSUS', 'CALIGOSUS', 'CALIGO', 'CALIGULA', 'CALIGULA',
        'CALINA', 'CALIPASH', 'CALISTANIA', 'CALISTA', 'CALITA', 'CALIZONUS', 'CALLA', 'CALLAIA', 'CALLAN', 'CALLEDA',
        'CALLENA', 'CALLENSIS', 'CALLENTIA', 'CALLENTOR', 'CALLEORIA', 'CALLERIA', 'CALLEROS', 'CALLETA', 'CALLETO', 'CALLEZA',
        'CALLICIA', 'CALLIDA', 'CALLIDITAS', 'CALLIDUS', 'CALLINA', 'CALLINO', 'CALLIS', 'CALLISTA', 'CALLITO', 'CALLIZA'
    ]
    
    def __init__(self, width=30, height=30):
        """Initialize word search with dimensions."""
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.words_placed = []
        self.directions = [
            (0, 1),   # right
            (1, 0),   # down
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
            (0, -1),  # left
            (-1, 0),  # up
            (-1, -1), # diagonal up-left
            (-1, 1)   # diagonal up-right
        ]
    
    def can_place_word(self, word, row, col, direction):
        """Check if a word can be placed at given position and direction."""
        dr, dc = direction
        
        for i, letter in enumerate(word):
            r = row + i * dr
            c = col + i * dc
            
            # Check bounds
            if r < 0 or r >= self.height or c < 0 or c >= self.width:
                return False
            
            # Check if cell is empty or matches letter
            cell = self.grid[r][c]
            if cell != ' ' and cell != letter:
                return False
        
        return True
    
    def place_word(self, word, row, col, direction):
        """Place a word on the grid."""
        dr, dc = direction
        
        for i, letter in enumerate(word):
            r = row + i * dr
            c = col + i * dc
            self.grid[r][c] = letter
        
        self.words_placed.append((word, row, col, direction))
    
    def generate(self):
        """Generate the word search puzzle."""
        random.shuffle(self.LATIN_WORDS)
        
        for word in self.LATIN_WORDS:
            placed = False
            attempts = 0
            
            while not placed and attempts < 50:
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - 1)
                direction = random.choice(self.directions)
                
                if self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True
                
                attempts += 1
        
        # Fill empty cells with random letters
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice(string.ascii_uppercase)
    
    def print_puzzle(self):
        """Print the word search puzzle."""
        print("\n=== LATIN WORD SEARCH PUZZLE ===\n")
        for row in self.grid:
            print(' '.join(row))
    
    def print_solution(self):
        """Print the puzzle with answers highlighted."""
        print("\n=== SOLUTION ===\n")
        solution_grid = [row[:] for row in self.grid]
        
        for row in solution_grid:
            print(' '.join(row))
        
        print(f"\n{len(self.words_placed)} words placed:")
        for i, (word, row, col, direction) in enumerate(self.words_placed, 1):
            dir_name = self.direction_name(direction)
            print(f"{i:3d}. {word:15s} at ({row:2d}, {col:2d}) going {dir_name}")
    
    def print_word_list(self):
        """Print list of words to find."""
        print("\n=== WORDS TO FIND ===\n")
        words = sorted([word for word, _, _, _ in self.words_placed])
        
        # Print in columns
        cols = 5
        for i in range(0, len(words), cols):
            row_words = words[i:i+cols]
            print("  ".join(f"{word:15s}" for word in row_words))
    
    def direction_name(self, direction):
        """Convert direction tuple to name."""
        directions = {
            (0, 1): "right",
            (1, 0): "down",
            (1, 1): "diagonal ↘",
            (1, -1): "diagonal ↙",
            (0, -1): "left",
            (-1, 0): "up",
            (-1, -1): "diagonal ↖",
            (-1, 1): "diagonal ↗"
        }
        return directions.get(direction, "unknown")
    
    def export_to_file(self, filename="latin_wordsearch.txt"):
        """Export puzzle to a text file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("LATIN WORD SEARCH - 100 WORDS\n")
            f.write("="*60 + "\n\n")
            
            f.write("PUZZLE:\n")
            f.write("-"*60 + "\n")
            for row in self.grid:
                f.write(' '.join(row) + '\n')
            
            f.write("\n" + "-"*60 + "\n")
            f.write("WORDS TO FIND:\n")
            f.write("-"*60 + "\n")
            words = sorted([word for word, _, _, _ in self.words_placed])
            cols = 5
            for i in range(0, len(words), cols):
                row_words = words[i:i+cols]
                f.write("  ".join(f"{word:15s}" for word in row_words) + '\n')
            
            f.write("\n" + "="*60 + "\n")
            f.write("SOLUTION:\n")
            f.write("="*60 + "\n\n")
            for row in self.grid:
                f.write(' '.join(row) + '\n')
            
            f.write("\n" + "-"*60 + "\n")
            f.write("WORD LOCATIONS:\n")
            f.write("-"*60 + "\n")
            for i, (word, row, col, direction) in enumerate(sorted(self.words_placed), 1):
                dir_name = self.direction_name(direction)
                f.write(f"{i:3d}. {word:15s} at row {row:2d}, col {col:2d} ({dir_name})\n")
        
        print(f"\nPuzzle exported to {filename}")


def main():
    """Main function to generate and display the word search."""
    # Create word search with 30x30 grid to fit 100 words
    ws = LatinWordSearch(width=40, height=40)
    
    # Generate the puzzle
    print("Generating Latin word search with 100 words...")
    ws.generate()
    
    # Display puzzle
    ws.print_puzzle()
    
    # Display words to find
    ws.print_word_list()
    
    # Display solution
    ws.print_solution()
    
    # Export to file
    ws.export_to_file()


if __name__ == "__main__":
    main()
