from hidden import Puzzle

# The number of the puzzle
puzzle = Puzzle(1)

# A list of randomly generated numbers
numbers = puzzle.get_input()
print(numbers)

# Set the variable 'answer' to your answer
answer = None

puzzle.test_answer(answer)
