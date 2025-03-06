# MiniProject 1:
# Today's project is actually a very common interview question, which revolves around a childhood counting game called Fizz Buzz.
# In case you're not familiar with the game, it goes like this:
# One player starts by saying the number 1.
# Each player then takes it in turns to say the next number, counting one at a time.
# If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
# If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
# If the number is divisible by 3 and 5, instead of saying the number, the player should say, "Fizz Buzz".
# If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.
# The player has to answer the question till the number he/she entered.
# The player has to answer as per the rules of the game.

import random

def fizz_buzz_game():
    number = int(input("Enter the range of numbers: "))
    max_range = int(input("Enter the maximum range for random number: "))
    score = 0
    last_number = 0

    for i in range(number):
        random_number = random.randint(0, max_range)
        i = last_number + random_number
        print(f"Random number: {random_number}")
        print(f"Number: {i}")
        last_number = i
        print("Choose the correct option:")
        print("1. Fizz")
        print("2. Buzz")
        print("3. Fizz Buzz")
        print("4. N/A")
        answer = int(input("Your choice: "))

        answers = ["Fizz", "Buzz", "Fizz Buzz", "N/A"]  # Answers list

        if i % 3 == 0 and i % 5 == 0:  # Fizz Buzz
            correct_answer = 3
        elif i % 3 == 0:  # Fizz
            correct_answer = 1
        elif i % 5 == 0:  # Buzz
            correct_answer = 2
        else:  # N/A
            correct_answer = 4

        if answer == correct_answer:  # Correct answer
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {answers[correct_answer - 1]}")  # Show correct answer from answers list with -1 index for correct answer
            break

    print(f"Total score is: {score}")

fizz_buzz_game()
