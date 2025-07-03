from project import (
    winning_line,
    row_winner,
    column_winner,
    main_diagonal_winner,
    diagonal_winner,
    winner,
    make_board,
    draw,
)

def test_winning_line():
    assert winning_line(['X', 'X', 'X']) is True
    assert winning_line([' ', ' ', ' ']) is False
    assert winning_line(['X', ' ', 'X']) is False

def test_row_winner():
    board = [
        ['X', 'X', 'X'],
        ['O', ' ', ' '],
        [' ', 'O', ' ']
    ]
    assert row_winner(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert row_winner(board) is False

def test_column_winner():
    board = [
        ['X', 'O', ' '],
        ['X', 'O', ' '],
        ['X', ' ', ' ']
    ]
    assert column_winner(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert column_winner(board) is False

def test_main_diagonal_winner():
    board = [
        ['X', 'O', ' '],
        ['O', 'X', 'O'],
        [' ', ' ', 'X']
    ]
    assert main_diagonal_winner(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', 'O', 'X']
    ]
    assert main_diagonal_winner(board) is False

def test_diagonal_winner():
    board = [
        [' ', ' ', 'X'],
        [' ', 'X', 'O'],
        ['X', ' ', ' ']
    ]
    assert diagonal_winner(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    assert diagonal_winner(board) is False

def test_winner():
    board = [
        ['O', 'O', 'O'],
        ['X', ' ', ' '],
        [' ', 'X', ' ']
    ]
    assert winner(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert winner(board) is False

def test_make_board():
    board = make_board(3)
    assert board == [[' '] * 3 for _ in range(3)]

    board = make_board(2)
    assert board == [[' ', ' '], [' ', ' ']]

def test_draw():
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert draw(board) is True

    board = [
        ['X', 'O', 'X'],
        ['O', ' ', 'O'],
        ['O', 'X', 'O']
    ]
    assert draw(board) is False
