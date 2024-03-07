from replit import clear
from art import logo

print(logo)
bidders = {}
ongoing = True


def find_highest_bid(bids):
    highest_bid = 0
    winner = ''
    for bid in bids:
        if bids[bid] > highest_bid:
            highest_bid = (bids[bid])
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while ongoing:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bidders[name] = price
    other_players = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if other_players == 'yes':
        clear()
    elif other_players == 'no':
        find_highest_bid(bidders)
        ongoing = False
