def checkio(matrix):
    #replace this for solution
    def its_valid(i, j):
        return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            count = 1
            for k in range(1, 4):
                if not its_valid(i, j + k):
                    break
                if value == matrix[i][j + k]:
                    count += 1
                else:
                    break
            if count == 4:
                return True
            count = 1
            for k in range(1, 4):
                if not its_valid(i + k, j):
                    break
                if value == matrix[i + k][j]:
                    count += 1
                else:
                    break
            if count == 4:
                return True
            count = 1
            for k in range(1, 4):
                if not its_valid(i + k, j + k):
                    break
                if value == matrix[i + k][j + k]:
                    count += 1
                else:
                    break
            if count == 4:
                return True
            count = 1
            for k in range(1, 4):
                if not its_valid(i + k, j - k):
                    break
                if value == matrix[i + k][j - k]:
                    count += 1
                else:
                    break
            if count == 4:
                return True


    return False
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
