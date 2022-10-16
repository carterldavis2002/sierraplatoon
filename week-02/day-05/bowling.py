from player import Player
from frame import Frame
import random

class Game:
    def __init__(self, players):
        self.players = [Player() for _ in range(players)]

    def play(self):
        turn = 0
        frame = 0
        while frame < 10:
            first = 10#random.randint(0, 10)
            second = 0#random.randint(0, 10 - first)
            if frame != 9:
                self.players[turn].add_frame(first, second)
            else:
                self.players[turn].add_frame(first, second)

            turn += 1
            if turn >= len(self.players):
                turn = 0
                frame += 1