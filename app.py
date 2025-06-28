# app.py
from flask import Flask, render_template, jsonify, request
import random
from sudokuGenerator import SudokuGenerator # Import your SudokuGenerator class

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main Sudoku game page."""
    return render_template('index.html')

@app.route('/generate_puzzle', methods=['POST'])
def generate_puzzle_endpoint():
    """
    API endpoint to generate a new Sudoku puzzle based on difficulty level.
    Returns the puzzle, its solution, difficulty, and clue count as JSON.
    """
    level = request.json.get('level', 'easy') # Default to 'easy' if not provided
    generator = SudokuGenerator()

    # Define the exact number of missing cells for each difficulty
    num_missing = {
        'easy': 18,
        'medium': 38,
        'hard': 48
    }

    # Get the target missing cells for the selected level, default to easy if level not found
    target_missing_cells = num_missing.get(level, num_missing['easy'])

    # The generate_puzzle method now directly takes num_missing_cells
    puzzle, solution = generator.generate_puzzle(target_missing_cells)

    # Classify difficulty based on the actual number of missing cells in the generated puzzle
    # (which might be slightly less than target_missing_cells if uniqueness couldn't be maintained)
    difficulty = generator.classify_difficulty(puzzle)
    clues_count = sum(1 for row in puzzle for cell in row if cell != 0)

    return jsonify({
        'puzzle': puzzle,
        'solution': solution, # Send solution for client-side checking/hinting
        'difficulty': difficulty,
        'clues': clues_count,
        'missing_cells': 81 - clues_count # Explicitly report missing cells
    })

@app.route('/solve_puzzle', methods=['POST'])
def solve_puzzle_endpoint():
    """
    API endpoint to solve a given Sudoku puzzle.
    This can be used to provide hints or check user's work.
    """
    puzzle_data = request.json.get('puzzle')
    if not puzzle_data:
        return jsonify({'error': 'No puzzle data provided'}), 400

    solver = SudokuGenerator()
    # Call solve_sudoku, which now returns the solved grid if unique
    solved_grid = solver.solve_sudoku(puzzle_data) # Pass the user's current grid state

    if solved_grid: # If a unique solution was found and returned
        return jsonify({'solution': solved_grid})
    elif solver.solutions_count > 1:
        return jsonify({'error': 'Puzzle has multiple solutions. Cannot provide a unique solution.'}), 400
    else: # solver.solutions_count == 0
        return jsonify({'error': 'Puzzle has no solution. Please check your input.'}), 400


if __name__ == '__main__':
    app.run(debug=True)