def checkio(text: str) -> str:

    data = []
    for e in text:
        if e.isalpha():
            data.append(e.lower())
    counts = []
    for d in data:
        counts.append(data.count(d))
    max = counts[0]
    current_alpha = data[0]
    for d, c in zip(data, counts):
        if c > max:
            current_alpha = d
            max = c
        elif c == max  and current_alpha > d:
            current_alpha = d
            max = c
    return current_alpha

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
