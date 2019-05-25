def time_converter(time):
    if time == "00:00":
        return "12:00 a.m."
    t = time.split(":")
    res = ""
    if int(t[0]) > 12:
        res += str(int(t[0]) % (12 + 1) + 1)
    else:
        res += str(int(t[0]))
    res += ":"
    res += t[1]
    res += " "
    if int(t[0]) > 11:
        res += "p.m."
    else:
        res += "a.m."
    #print(res)
    return res

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
