"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

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
    c = 0
    for a in board:
        for b in a:
            if b != EMPTY:
                c += 1
    return O if c % 2 != 0 else X


def actions(board):
    r = set()
    l = len(board)
    for row in range(l):
        for col in range(l):
            if board[row][col] == EMPTY:
                t = (row, col)
                r.add(t)
    return r


def result(board, action):
    b = deepcopy(board)
    p = player(b)
    r, c = action
    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
        raise Exception("Action out of bounds")
    if b[r][c]!=None:
        raise Exception("Cell already occupied")
    b[r][c] = p

    return b


def check(x):
    return len(set(x)) == 1 and x[0] != EMPTY


def winner(board):
    l = len(board)
    # p=player(board)
    for n in board:
        if check(n):
            return n[0]
    for a in range(l):
        r = []
        for b in range(l):
            r.append(board[b][a])
        if check(r):
            return r[0]
    r = []
    for b in range(l):
        r.append(board[b][b])
    if check(r):
        return r[0]
    r = []
    for b in range(l):
        r.append(board[b][l-b-1])
    if check(r):
        return r[0]
    return None


def terminal(board):
    if winner(board) != None:
        return True
    for n in board:
        for _ in n:
            if _ == EMPTY:
                return False
    return True


def utility(board):
    w = winner(board)
    if w == "X":
        return 1
    elif w == "O":
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board) == True:
        return None
    best = None
    p = player(board)
    if p == "X":
        init = -2
    else:
        init = 2
    for n in actions(board):
        res = result(board, n)
        if terminal(res):
            v = utility(res)
        else:
            v = custom(res)
        if p == "X" and v > init:
            init = v
            best = n
        elif p == "O" and v < init:
            init = v
            best = n
    return best


def custom(board):
    v = []
    p = player(board)
    for n in actions(board):
        res = result(board, n)
        if terminal(res):
            u = utility(res)
            if p == X and u == 1:
                return u
            if p == O and u == -1:
                return u
            v.append(u)
        else:
            c = custom(res)
            if p == X and c == 1:
                return c
            if p == O and c == -1:
                return c
            v.append(c)
    if not v:
        return 0
    return max(v) if p == X else min(v)
#minmax algorithm
#with alpha beta pruning
