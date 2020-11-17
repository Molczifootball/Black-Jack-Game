############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from deck import *
from art import *

my_deck = []
cpu_deck = []
def set_ace_val(card1,card2):
    if 21 - 11 - card2 > 21 - 2 - card2:
        return 2
    elif 21 - 11 - card2 < 21 - 2 -card2:
        return 11

def roll(deck):
    result = 0 
    deck.append(common_deck[random.randint(0,(len(common_deck)-1))])
    deck.append(common_deck[random.randint(0,(len(common_deck)-1))])
    card1_val = deck[0]["Value"]
    card2_val = deck[1]["Value"]
    if deck[0]["Name"] == "Ace":
        card1_val = set_ace_val(card1_val,card2_val)
    elif deck[1]["Name"] == "Ace":
        card2_val = set_ace_val(card2_val,card1_val)
    elif deck[1]["Name"] == "Ace" and deck[0]["Name"] == "Ace":
        card1_val = set_ace_val(card1_val,card2_val)
      
print(logo)
roll(my_deck)
roll(cpu_deck)
my_result = my_deck[0]["Value"] + my_deck[1]["Value"]
cpu_result = cpu_deck[0]["Value"] + cpu_deck[1]["Value"]
my_card1 = my_deck[0]["Name"]
my_card2 = my_deck[1]["Name"]
cpu_card1 = cpu_deck[0]["Name"]
cpu_card2 = cpu_deck[1]["Name"]
print(f"Player cards are: {my_card1} and {my_card2} with the result of {my_result}")
print(f"Player cards are: {cpu_card1} and {cpu_card2} with the result of {cpu_result}")

if cpu_result > 21:
    print("Player won")
elif my_result > 21:
    print("CPU won")
elif cpu_result >21 and my_result > 21:
    print("TIE")
else:
    if 21- my_result < 21-cpu_result:
        print("Player won.")
    elif 21 - my_result > 21 - cpu_result:
        print("CPU won.")
    else:
        print("TIE.")