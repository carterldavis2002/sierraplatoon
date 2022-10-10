class GuessingGame:

    def __init__(self, answer):
        self.answer = answer
        self.last_guess = answer - 1

    def guess(self, user_guess):
        user_guess = int(user_guess)
        self.last_guess = user_guess
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        else:
            return "correct"

    def solved(self):
        return self.last_guess == self.answer