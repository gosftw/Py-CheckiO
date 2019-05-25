def sun_angle(time):
    #replace this for solution
    t = list(map(int, time.split(":")))
    mins = t[0] * 60 + t[1]
    mins -= 360
    if mins < 0 or mins > 720:
        return "I don't see the sun!"
    return mins / 4

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
