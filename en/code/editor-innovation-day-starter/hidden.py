secret_number = 5

def test_solution(answer):
    if answer == secret_number:
        print("You're the winner!")
    else:
        print("Sorry, that wasn't correct")