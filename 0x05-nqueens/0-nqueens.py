#!/usr/bin/python3

"""Method that calculates the non-attacking nqueens of
n * n board - Check the README.md file for detailed info"""

import sys


def ChessBoard(n: int):
    """Program that solves the N queens problem with
    Backtracking algorithm
    Args:
        n (int): no of non-attacking queens to place on board.
                (n)^2 determines the size of chess board

    Return:
        List[List[int]]: List of list of rows & columns of where
        queens are placed.
    """
    result = list()

    def checkBoard(row, col, col_in_row):
        """Checks if queen can be placed without attacking other queens"""
        for r in range(row):
            if col == col_in_row[r] or abs(row - r) == abs(col - col_in_row[r]):
                return False
        return True

    def saveBoard(row, cols, col_in_row):
        """Saves the current state (position of the queens) of the board"""
        if row == n:
            con_result = []
            for r in range(n):
                con_result.append([r, col_in_row[r]])
            result.append(con_result)

    def placeQueen(row, cols, col_in_row):
        """Places N non-attacking queens on an N * N chessboard"""
        if row == n:
            saveBoard(row, cols, col_in_row)
            return
        for col in range(n):
            if cols[col] == 0 and checkBoard(row, col, col_in_row):
                cols[col] = 1
                col_in_row[row] = col
                placeQueen(row + 1, cols, col_in_row)
                cols[col] = 0
    placeQueen(0, [0]*n, [0]*n)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = ChessBoard(N)
    for queens in nqueens:
        print(queens)

