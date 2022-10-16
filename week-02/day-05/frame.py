class Frame:
    def __init__(self, pins):
        self.pins = pins
        self.strike = pins[0] == 10
        self.spare = pins[0] + pins[1] == 10 and pins[0] != 10

    def __str__(self):
        return f"{self.pins} Strike: {self.strike} Spare: {self.spare}"