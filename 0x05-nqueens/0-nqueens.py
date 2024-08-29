#!/usr/bin/python3
"""0-nqueens.py"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    """
    Recursively solve the N queens problem and print all solutions
    """
    if row == n:
        print([[i, j] for i in range(n) for j in range(n) if board[i][j] == 1])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for j in range(N)] for i in range(N)]
    solve(board, 0, N)

