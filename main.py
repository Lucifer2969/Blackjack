import random
deck_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_list = []
computer_list = []

def user_card_shuffle():
    user_list.append(random.choice(deck_list))

def computer_card_shuffle():
    computer_list.append(random.choice(deck_list))

