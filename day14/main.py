import random
from game_data import data
from art import logo, vs

data = data

def retreive_account(data):
    data = data
    entry = random.choice(data)
    return entry

def compare_accounts(a,b):
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if a_count > b_count:
        return a["name"]
    elif a_count < b_count:
        return b["name"]
    elif a_count == b_count:
        return "draw"

def check_winner(entry, guess):
    if entry == guess:
        return 1
    else:
        return 0

def play_game():
    account_a = retreive_account(data)
    account_b = retreive_account(data)
    compare = compare_accounts(account_a,account_b)

    score = 0
    ongoing = True

    print(logo)
    while ongoing:
        while account_a == account_b:
            account_b = retreive_account(data)

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == 'A' or guess == 'a':
            guess = account_a['name']
        elif guess == 'B' or guess == 'b':
            guess = account_b['name']

        winner = check_winner(compare, guess)

        if winner == 0:
            print(f"Sorry, that's wrong. Final score: {score}")
            ongoing = False
        else:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b
            account_b = retreive_account(data)

play_game()