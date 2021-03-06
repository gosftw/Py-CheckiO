FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    result = ""
    residuo = number % 100
    if residuo > 0:
        if residuo > 19:
            result = result + OTHER_TENS[(residuo // 10) - 2]
            if residuo % 10 > 0:
                result = result + " " +FIRST_TEN[(residuo % 10) - 1]
        elif residuo < 10:
            result = result + FIRST_TEN[residuo - 1]
        else:
            result = result + SECOND_TEN[residuo % 10]
    number = number // 100
    if number > 0:
        result = FIRST_TEN[number - 1] + " " + HUNDRED + " " + result

    return result.strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
