"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board) == False:
        if sum(x.count("X") for x in board) > sum(x.count("O") for x in board):
            return "O"
        else:
            return "X"
    else:
        return


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == False:
        actions = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    actions.add((i, j))
        return actions
    else:
        return


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action")
    elif action[0] < 0 or action[0] > 3 or action[1] < 0 or action[1] > 3:
        raise Exception("Out of bounds move")
    else:
        deep_copied_board = copy.deepcopy(board)
        deep_copied_board[action[0]][action[1]] = player(board)
        return deep_copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or
        board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X" or
        board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or
        board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or
        board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or
        board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or
        board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or
            board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        return "X"
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or
          board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O" or
          board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or
          board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or
          board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or
          board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or
          board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or
          board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        return "O"
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if (winner(board) == "X" or winner(board) == "O" or count == 9):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    best_action = None
    if player(board) == "X":
        best_value = float('-inf')
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = float('inf')
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value < best_value:
                best_value = value
                best_action = action

    return (best_action)


def minimax_value(board):
    if terminal(board):
        return utility(board)

    if player(board) == "X":
        best_value = float('-inf')
        for action in actions(board):
            new_board = result(board, action)
            best_value = max(best_value, minimax_value(new_board))
    else:
        best_value = float('inf')
        for action in actions(board):
            new_board = result(board, action)
            best_value = min(best_value, minimax_value(new_board))

    return best_value
