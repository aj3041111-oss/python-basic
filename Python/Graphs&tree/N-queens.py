def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):

    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n)


n = 4
board = [-1] * n

solve(board, 0, n)