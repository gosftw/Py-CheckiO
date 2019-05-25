def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    try:
        init = text.index(begin)
    except:
        init = -1
    try:
        e = text.index(end)
    except:
        e = -1
    if init >= 0 and e >= 0:
        return text[init + len(begin):e]
    elif init>= 0 and e <0:
        return text[init + len(begin):]
    elif init < 0 and e  >= 0:
        return text[: e]
    elif init < 0 and e < 0:
        return text
    return ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
