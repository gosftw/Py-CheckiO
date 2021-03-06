# Taken from mission The Warriors
class Army:
    def __init__(self):
        self.army = []
        self.alive_pos = 0

    def add_units(self, cls, count):
        for _ in range(count):
            self.army.append(cls())

    @property
    def have_alive(self):
        return self.alive_pos < len(self.army)

class Battle:

    def fight(self, army_A, army_B):
        turn = True
        while army_A.have_alive and army_B.have_alive:
            if turn:
                army_B.army[army_B.alive_pos].health -= army_A.army[army_A.alive_pos].attack
                if not army_B.army[army_B.alive_pos].is_alive:
                    army_B.alive_pos += 1
            else:
                army_A.army[army_A.alive_pos].health -= army_B.army[army_B.alive_pos].attack
                if not army_A.army[army_A.alive_pos].is_alive:
                    army_A.alive_pos += 1
            turn = not turn
        if army_A.have_alive:
            return True
        else:
            return False


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

class Knight(Warrior):

    def __init__(self):
        self.health = 50
        self.attack = 7

def fight(unit_1, unit_2):
    turn = True
    while unit_1.is_alive and unit_2.is_alive:
        if turn:
            unit_2.health -= unit_1.attack
        else:
            unit_1.health -= unit_2.attack
        turn = not turn
    if unit_1.is_alive:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
