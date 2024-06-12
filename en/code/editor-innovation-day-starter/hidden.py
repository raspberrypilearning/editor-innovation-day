from random import randint, seed

# Generate a test input of a bunch of random numbers
secret = [randint(0,1000) for i in range(40)]

def view_input():
    print(secret)

# Trivial example - calculate the largest number
def calculate_solution(current_input):
    return max(current_input)

# Test their solution
def test_my_answer(answer=None):
    if answer is None:
        print("Put your answer in the brackets, e.g. test_my_answer(0)")
    elif answer == calculate_solution(secret):
        print("Well done, you are correct!")
    else:
        print("Sorry, you're wrong. Try again!")