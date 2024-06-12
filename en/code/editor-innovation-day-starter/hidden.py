from random import randint

class Challenge():

    def __init__(self, step):
        self.step = step
        self.secret = None

        self.set_input() # Init input according to the step
    
    def set_input(self):
        """
        Sets the secret input for the given step
        """
        match self.step:
            case 1 | 2:
                self.secret = [randint(0,1000) for i in range(40)]
            case _:
                print(f"Error initialising challenge {self.step}")

    def get_input(self):
        """
        Returns the secret input for the current step
        """
        return self.secret

    def calculate_solution(self):
        """
        Calculates the solution for the current step
        """
        match self.step:
            case 1:
                return max(self.secret)
            case 2:
                return min(self.secret)
            case _:
                print(f"Error calculating answer for {self.step}")

    def test_answer(self, answer=None):
        """
        Checks the answer provided
        """
        if answer is None:
            print("The variable 'answer' should contain your solution")
        elif answer == self.calculate_solution():
            print("Well done, you are correct!")
        else:
            print("Sorry, you're wrong. Try again!")


   