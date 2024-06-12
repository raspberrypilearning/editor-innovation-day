from random import randint

class Puzzle():

    def __init__(self, step):
        self.step = step
        self.secret = None
        self.description = {1: "Find the largest number", 2: "Find the smallest number", 3: "How many of the numbers are even?"}

        self.set_input() # Init input according to the step
    
    def set_input(self):
        """
        Sets the secret input for the given step
        """
        if self.step > 0:
            self.secret = [randint(0,1000) for i in range(10)]
        else:
            print(f"Error initialising challenge {self.step}")
    
    def get_description(self):
        return self.description[self.step]

    def get_input(self):
        """
        Returns the secret input for the current step
        """
        return self.secret

    def calculate_solution(self):
        """
        Calculates the solution for the current step
        """
        if self.step == 1:
            return max(self.secret)
        elif self.step == 2:
            return min(self.secret)
        elif self.step == 3:
            new_list = [n%2==0 for n in self.secret]
            return new_list.count(True)
        else:
            print(f"Error calculating answer for {self.step}")

    def test_answer(self, answer=None):
        """
        Checks the answer provided
        """
        print(f"------------------------------")
        print(f"Puzzle #{self.step} - {self.get_description()}")
        print(f"The input was: {self.secret}")
        print(f"------------------------------")
        if answer is None:
            print("The variable 'answer' should contain your solution")
        elif answer == self.calculate_solution():
            print(f"Your answer was: {answer}")
            print(f"Well done, you got puzzle {self.step} correct!")
        else:
            print(f"Your answer was: {answer}")
            print(f"Sorry, you're wrong.")
            if type(answer) is not type(self.calculate_solution()):
                print(f"Your answer was a {type(answer).__name__}, but it should be {type(self.calculate_solution()).__name__}")


   