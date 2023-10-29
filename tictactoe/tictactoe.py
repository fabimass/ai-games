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
    count_X = 0
    count_O = 0
    
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)
    
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    candidates = set()
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                candidates.add((i,j))

    return candidates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Verify that the action is a tuple
    if not isinstance(action, tuple):
        raise TypeError("Invalid action: the action must be a tuple")
    
    # Verify that the action is made only of 2 elements
    if not len(action) == 2:
        raise TypeError("Invalid action: the action must have only 2 elements")
    
    # Check if all elements in the tuple are 0, 1, or 2
    for element in action:
        if element not in (0, 1, 2):
            raise TypeError("Invalid action: the action contains invalid coordinates")
    
    # Get which player moves next
    player_turn = player(board)

    # Make a deep copy of the current board
    new_board = copy.deepcopy(board)

    # Make the movement
    new_board[action[0]][action[1]] = player_turn
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    # Check for winner row
    for row in board:
        if all(element == X for element in row):
            winner = X
        elif all(element == O for element in row):
            winner = O

    # Check for winner column
    columns = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]
    for column in columns:
        if all(element == X for element in column):
            winner = X
        elif all(element == O for element in column):
            winner = O

    # Check for winner diagonal
    diagonals = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    for diagonal in diagonals:
        if all(element == X for element in diagonal):
            winner = X
        elif all(element == O for element in diagonal):
            winner = O

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Checks if there is a winner
    if winner(board):
        return True
    
    # Checks if there are empty cells
    for row in board:
        if None in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # Gets the possible next movements
    candidates = actions(board)

    if player(board) == X:
        # X is trying to maximize the value
        return max(candidates, key=lambda action: min_value(result(board, action)))
    
    else:
        # O is trying to minimize the value
        return min(candidates, key=lambda action: max_value(result(board, action)))


def max_value(board, pruning_value=100):
    """
    Returns the value of the state when I'm trying to maximize the value.
    """

    if terminal(board):
        return utility(board)
    
    value = -100

    for action in actions(board):
        value = max(value, min_value(result(board, action), value))
        if value >= pruning_value:
            break

    return value


def min_value(board, pruning_value=-100):
    """
    Returns the value of the state when I'm trying to minimize the value.
    """

    if terminal(board):
        return utility(board)
    
    value = 100

    for action in actions(board):
        value = min(value, max_value(result(board, action), value))
        if value <= pruning_value:
            break
    
    return value
