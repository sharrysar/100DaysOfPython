import random

def number_check(number, guess):
    if guess < number:
        return "low"
    elif guess > number:
        return "high"
    elif guess == number:
        return f"equal"
    
def play_game():

    options = [i for i in range(1, 101)]
    number = random.choice(options)
    ongoing = True

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        available_attempts = 10
    elif difficulty == 'hard':
        available_attempts = 5
    else:
        print("Invalid input. Run the program again.")
        exit()

    while ongoing:
        print(f"You have {available_attempts} remaining to guess the number. ")
        if available_attempts == 0:
            print("Game over! You ran out of attempts.")
            break
        guess = int(input("Make a guess: "))
        check = number_check(number, guess)
        if check == 'low':
            print("Too low.")
            available_attempts -= 1
        elif check == 'high':
            print("Too high.")
            available_attempts -= 1
        elif check == 'equal':
            print(f"You got it! The answer was {number}.")
            ongoing = False

play_game()