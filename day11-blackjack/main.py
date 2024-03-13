from art import logo
import random

# play_game = input("Play game? y/n: ")

# if play_game == 'y':
#     clear()



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if 10 in cards and 11 in cards and score == 21:
        return 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(player_score, dealer_score):
    
    if player_score == 21:
        return "Blackjack. You win!"
    elif player_score > 21:
        return f"You scored {player_score}. Dealer wins!"
    elif dealer_score == 21:
        return "Blackjack. Dealer wins!"
    elif dealer_score > 21:
        return f"Dealer scored {dealer_score}. You win!"
    elif player_score > dealer_score:
        return f"Your score: {player_score}\nDealer score: {dealer_score}.\nYou win!"
    elif player_score < dealer_score:
        return f"Your score: {player_score}\nDealer score: {dealer_score}.\nDealer wins!"
    elif player_score == dealer_score:
        return "It's a draw!"

def play_game():
    print(logo)
    player_cards = []
    dealer_cards = []
    ongoing = True

    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while ongoing:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"    Your cards are: {player_cards}. Your score: {player_score}")
        print(f"    Dealer's first card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            ongoing = False
        else:
            new_card = input("Type 'y' to get a new card, type 'n' to pass: ")
            if new_card == 'y':
                player_cards.append(deal_card())
            else:
                ongoing = False

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"    Your cards: {player_cards}. Your score: {player_score}")
    print(f"    Dealer's cards: {dealer_cards}. Dealer's score: {dealer_score}")
    print(compare(player_score, dealer_score))

play_game()