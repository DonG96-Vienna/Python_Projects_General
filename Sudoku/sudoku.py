'''

Sudoku Spiel mithilfe von einer Rekursion
Brute-Force Methode - Alle Optionen werden getestet

'''

import pprint

# Funktion um den nächsten noch leeren Spot zu finden
# Wenn alle belegt, dann wird None returned --> gelöst
def next_empty_spot(sudoku):

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r, c

    return None, None

# Checken ob guess in der Zeile, Spalte oder 3x3 Block ist
def is_valid(guess, sudoku, row, col):

    if guess in sudoku[row]:
        return False

    for i in range(9):
        if guess == sudoku[i][col]:
            return False

    row_0 = (row//3)*3
    col_0 = (col//3)*3

    for r in range(row_0, row_0+3):
        for c in range(col_0, col_0+3):
            if sudoku[r][c] == guess:
                return False
    return True

# main function. Verwendet einen Rekursionsaufruf um bei Fehler zurückzugehen und alle Möglichkeiten zu probieren
def solve_sudoku(sudoku):

    row, col = next_empty_spot(sudoku)

    #print(f"({row},{col})") /zum Testen

    if row is None:
        return True

    for guess in range(1, 10):

        #print(f"!{guess}") /zum Testen

        if is_valid(guess, sudoku, row, col):

            sudoku[row][col] = guess

            if solve_sudoku(sudoku):
                return True

        #print(f"!!{guess}") /zum Testen
        sudoku[row][col] = 0

        #print(f"!({row},{col})") /zum Testen

    return False

# Beliebiges Sudoku-Spiel eintippen und starten
if __name__ == '__main__':
    board = [
        [0, 0, 0, 4, 7, 0, 0, 3, 0],
        [0, 0, 4, 0, 0, 2, 0, 0, 0],
        [0, 0, 9, 5, 3, 0, 0, 6, 0],

        [5, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 8, 7, 9, 0, 0],
        [0, 9, 0, 0, 0, 0, 6, 0, 0],

        [0, 0, 6, 0, 4, 0, 0, 0, 0],
        [8, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 1, 2, 0, 0]
    ]

    print(solve_sudoku(board))
    pprint.pprint(board)