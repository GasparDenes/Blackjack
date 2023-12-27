############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
user_won = False
computer_won = False
new_game = True


def deal_cards():
    for i in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    print(f"User:{user} Computer:[{computer[0]}, X]")


def scores():
    global user_won
    global computer_won
    if sum(user) == 21:
        if sum(computer) == 21:
            user_won = True
            computer_won = True
        else:
            user_won = True
    elif sum(user) > 21:
        if sum(computer) > 21:
            user_won = True
            computer_won = True
        else:
            computer_won = True
    elif sum(computer) == 21 and sum(user) != 21:
        computer_won = True
    elif sum(computer) > 21 and sum(user) <= 21:
        user_won = True
    elif sum(user) < 21 and sum(computer) < 21:
        if sum(user) > sum(computer):
            user_won = True
        elif sum(user) < sum(computer):
            computer_won = True
        else:
            user_won = True
            computer_won = True
    return


def outcome():
    print(f"User: {user} Computer: {computer}")
    if user_won == True and computer_won == True:
        print("Draw!")
    elif user_won == True and computer_won == False:
        print("You Win!")
    elif computer_won == True and user_won == False:
        print("You Lost!")
    else:
        return


def rounds():
    while sum(user) < 21 and sum(computer) < 21:
        action = input("Do you want to draw another card? Type 'y' or 'n'")
        if action.lower() == "y":
            user.append(random.choice(cards))
            print(f"User:{user} Computer:[{computer[0]}, X]")
        elif action.lower() == "n":
            while sum(computer) <= 16:
                computer.append(random.choice(cards))
                print(f"User: {user} Computer: {computer}")
            return


while new_game:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    computer = []
    user_won = False
    computer_won = False
    print(logo)
    deal_cards()
    rounds()
    scores()
    outcome()
    again = input("Do you want to play again? Type'y'or'n'")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Do you want to play again? Type'y'or'n'")
    if again.lower() == 'n':
        new_game = False
    os.system('clear')
