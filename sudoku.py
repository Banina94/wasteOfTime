import random
from copy import deepcopy

class SudokuGenerator:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.solution = None
    
    def is_valid(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True
    
    def fill_board(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    def generate_solution(self):
        self.fill_board(self.board)
        self.solution = deepcopy(self.board)
    
    def generate_puzzle(self, difficulty="medium"):
        self.generate_solution()
        puzzle = deepcopy(self.solution)
        
        difficulty_map = {"easy": 45, "medium": 55, "hard": 58}
        cells_to_remove = difficulty_map.get(difficulty, 55)
        
        removed = 0
        while removed < cells_to_remove:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                removed += 1
        
        return puzzle
    
    def print_board(self, board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(board[i][j] if board[i][j] != 0 else ".", end=" ")
            print()

# Generate puzzles
generator = SudokuGenerator()

print("EASY PUZZLE (45 numbers missing):")
easy_puzzle = generator.generate_puzzle("easy")
generator.print_board(easy_puzzle)

print("\n\nEASY SOLUTION:")
generator.print_board(generator.solution)

print("\n\n" + "="*30)
generator = SudokuGenerator()

print("MEDIUM PUZZLE (55 numbers missing):")
medium_puzzle = generator.generate_puzzle("medium")
generator.print_board(medium_puzzle)

print("\n\nMEDIUM SOLUTION:")
generator.print_board(generator.solution)

print("\n\n" + "="*30)
generator = SudokuGenerator()

print("HARD PUZZLE (58 numbers missing):")
hard_puzzle = generator.generate_puzzle("hard")
generator.print_board(hard_puzzle)

print("\n\nHARD SOLUTION:")
generator.print_board(generator.solution)