VOWELS = "aeiouy"

def translate(phrase):
    result = []
    i = 0
    while i < (len(phrase)):
        result.append(phrase[i])
        if phrase[i] not in VOWELS and phrase[i].isalpha():
            i += 1
        elif phrase[i] in VOWELS:
            i += 2
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
