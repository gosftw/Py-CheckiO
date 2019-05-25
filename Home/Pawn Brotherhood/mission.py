def count_safe(mat) -> int:
    count = 0
    for i in range(1, 8):
        for j in range(8):
            if j > 0 and j < 7:
                if mat[i][j] == 1 and (mat[i - 1][j -1] == 1 or mat[i- 1][j + 1] == 1):
                    count += 1
            elif j == 0:
                if mat[i][j] == 1 and mat[i- 1][j + 1] == 1:
                    count += 1
            elif j == 7:
                if mat[i][j] == 1 and mat[i - 1][j -1] == 1:
                    count += 1
    return count

def safe_pawns(pawns: set) -> int:
    mat = [[0 for col in range(8)] for row in range(8)]
    for ele in pawns:
        pos_j = ord(ele[0]) - ord('a')
        pos_i = int(ele[1]) - 1
        mat[pos_i][pos_j] = 1
    return count_safe(mat)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
