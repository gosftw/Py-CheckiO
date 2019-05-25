def checkio(number: int) -> int:
    mul = 1
    while number > 0:
        res = number % 10
        if res != 0:
            mul *= res
        number = number // 10
    return mul


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
