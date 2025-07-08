"""
Tic Tac Toe Player
"""

import copy  # Needed for deepcopy

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()  # Fix: Indentation corrected
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    new_board = copy.deepcopy(board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action: cell already occupied")

    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns 'X' or 'O' if there is a winner on the board.
    Returns None if no winner.
    """
    lines = []

    # Add rows
    for row in board:
        lines.append(row)
    
    # Add columns
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])
    
    # Add diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    # Check each line for a winner
    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return line[0]  # 'X' or 'O'
    
    return None  # No winner


def terminal(board):
    # Count empty cells
    empty_count = 0
    for row in board:
        for cell in row:
            if cell is None:
                empty_count += 1
    
    # Game is over if there's a winner or no empty spaces
    return winner(board) is not None or empty_count == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0



def minimax(board):
    current_player = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state), None
        v = float('-inf')
        best_action = None
        for action in actions(state):
            min_v, _ = min_value(result(state, action))
            if min_v is not None and min_v > v:
                v = min_v
                best_action = action
        return v, best_action

    def min_value(state):
        if terminal(state):
            return utility(state), None
        v = float('inf')
        best_action = None
        for action in actions(state):
            max_v, _ = max_value(result(state, action))
            if max_v is not None and max_v < v:
                v = max_v
                best_action = action
        return v, best_action

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action
