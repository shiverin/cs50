def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings


def row_winner(board):
    return any(winning_line(row) for row in board)


def column_winner(board):
    return row_winner(zip(*board))


def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))


def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))


def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)


def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'


def play_move(board, symbol, player_name):
    print(f'{player_name} to play ({symbol}):')
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] == ' ':
                board[row][col] = symbol
                break
            else:
                print("Cell already taken, choose again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter numbers between 1 and 3.")
    print(format_board(board))


def make_board(size):
    return [[' '] * size for _ in range(size)]


def print_winner(player_name):
    print(f'{player_name} wins!')


def print_draw():
    print("It's a draw!")


def draw(board):
    return all(cell != ' ' for row in board for cell in row)


def play_game(board_size, symbol1, symbol2, name1, name2):
    board = make_board(board_size)
    print(format_board(board))

    current_player = 0
    players = [(symbol1, name1), (symbol2, name2)]

    while not winner(board):
        if draw(board):
            print_draw()
            return
        symbol, player_name = players[current_player]
        play_move(board, symbol, player_name)
        if winner(board):
            print_winner(player_name)
            return
        current_player = 1 - current_player  # Alternate players


def main():
    print("Player 1 name:")
    name1 = input()
    print("Symbol 1:")
    alpha = input()
    print("Player 2 name:")
    name2 = input()
    print("Symbol 2:")
    beta = input()
    while beta == alpha:
        print("Duplicate symbol, choose another:")
        beta = input()
    SIZE = 3
    play_game(SIZE, alpha, beta, name1, name2)


if __name__ == "__main__":
    main()
