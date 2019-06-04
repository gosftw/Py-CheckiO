def checkio(number: int) -> int:
    count = 0
    while number > 0:
        if number % 2 == 1:
            count += 1
        number //= 2
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
