class StateLamp:
    def show(self, context):
        pass


class GreenLamp(StateLamp):
    def show(self, context):
        context.set_state(RedLamp())
        return 'Green'


class RedLamp(StateLamp):
    def show(self, context):
        context.set_state(BlueLamp())
        return 'Red'


class BlueLamp(StateLamp):
    def show(self, context):
        context.set_state(YellowLamp())
        return 'Blue'


class YellowLamp(StateLamp):
    def show(self, context):
        context.set_state(GreenLamp())
        return 'Yellow'


class Lamp:

    def __init__(self):
        self.stateLamp = GreenLamp()

    def set_state(self, newState):
        self.stateLamp = newState

    def light(self):
        return self.stateLamp.show(self)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
