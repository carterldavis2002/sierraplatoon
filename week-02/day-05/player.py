from frame import Frame

class Player:
    def __init__(self):
        self.frames = []
        self.score = 0

    def add_frame(self, first, second):
        self.frames.append(Frame([first, second]))
        self.calculate_score()

    def calculate_score(self):
        score = 0
        for i in range(len(self.frames)):
            if not self.frames[i].spare and not self.frames[i].strike:
                score += self.frames[i].pins[0]
                score += self.frames[i].pins[1]
            elif self.frames[i].spare and i + 1 < len(self.frames):
                score += 10 + self.frames[i + 1].pins[0]
            else:
                if i + 1 < len(self.frames) and not self.frames[i + 1].strike:
                    score += 10
                    score += self.frames[i + 1].pins[0]
                    score += self.frames[i + 1].pins[1]
                elif i + 2 < len(self.frames) and self.frames[i + 1].strike:
                    score += 20
                    score += self.frames[i + 2].pins[0]
            

        self.score = score
        print(self.frames[len(self.frames) - 1])
        print(self.score)