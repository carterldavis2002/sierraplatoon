#GuessingGame class simulates a simple guessing game
class GuessingGame:

    #Initialize correct answer to passed answer

    #Set last guess to a number that is not answer so
    #the solved instance method will not return true before
    #a guess is made
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = answer - 1

    #Convert entered guess to an integer and set it to last guess

    #Return appropriate statement based on how the guess compares
    #to the answer
    def guess(self, user_guess):
        user_guess = int(user_guess)
        self.last_guess = user_guess
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        else:
            return "correct"

    #Game is solved if the previous guess was the answer
    def solved(self):
        return self.last_guess == self.answer