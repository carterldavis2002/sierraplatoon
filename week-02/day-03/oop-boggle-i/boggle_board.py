import random

class BoggleBoard:
    def __init__(self):
        self.board = [["_" for _ in range(4)] for _ in range(4)]
        self.dice = [[chr(random.randrange(65, 91)) for _ in range(6)] for _ in range(16)]

    def shake(self):
        counter = 0
        for i in range(4):
            for j in range(4):
                self.board[i][j] = self.dice[counter][random.randrange(0, 6)]
                counter += 1
    
    def __str__(self):
        board = ""
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == "Q":
                    board += "Qu" + " "
                else:
                    board += self.board[i][j] + "  "
            board += "\n"
        return board