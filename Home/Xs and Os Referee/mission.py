from typing import List

def check(mat, str) -> bool:
    for i in range(3):
        sum_row = 0
        sum_col = 0
        for j in range(3):
            if mat[i][j] == str:
                sum_row += 1
            if mat[j][i] == str:
                sum_col += 1
        if sum_row == 3 or sum_col == 3:
            return True
    if mat[0][0] == str and mat[1][1] == str and mat[2][2] == str:
        return True
    if mat[2][0] == str and mat[1][1] == str and mat[0][2] == str:
        return True
    return False

def checkio(game_result: List[str]) -> str:
    mat = []
    for line in game_result:
        mat.append(list(line))
    if check(mat, 'X'):
        return "X"
    if check(mat, 'O'):
        return 'O'
    return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
