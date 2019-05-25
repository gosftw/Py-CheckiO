def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if len(line) == 0:
        return 0
    current = line[0]
    max_count = 1
    count = 1
    for e in line[1:]:
        if e == current:
            count += 1
        else:
            count = 1;
        if count > max_count:
            max_count = count
        current = e
    return max_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
