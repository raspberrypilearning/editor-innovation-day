# Challenge 1

from random import randint, seed

# Generate a test input of a bunch of random numbers
secret = [randint(0,1000) for i in range(40)]

def view_input():
    return secret

# Trivial example - calculate the largest number
def calculate_solution(current_input):
    return max(current_input)

# Test their solution
def test_my_answer(answer=None):
    if answer is None or answer == 0:
        print("The variable 'answer' should contain your solution")
    elif answer == calculate_solution(secret):
        print("Well done, you are correct!")
    else:
        print("Sorry, you're wrong. Try again!")