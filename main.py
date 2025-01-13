import random
deck_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_list = []
computer_list = []

def user_card_shuffle():
    user_list.append(random.choice(deck_list))
    
def computer_card_shuffle():
    computer_list.append(random.choice(deck_list))

def user_hand_status():
    print(f"Your hand: {user_list} , Total {list_total(user_list)}")

def computer_hand_status():
    print(f"Computer hand: {computer_list} , Total {list_total(computer_list)}")

def list_total(list):
    return sum(list)

user_hand_status()
computer_hand_status()
for i in range(2):
    user_card_shuffle()
    computer_card_shuffle()

choice = input("Do you want to play the game of Blackjack? Type 'y' or 'n': ")
while choice == 'y':
    user_hand_status()
    print(f"Computer first card {computer_list[0]}")

    game_choice = input("Press 'y' to Draw another card and 'n' to Pass: ")

    if game_choice == 'y':
        user_card_shuffle()
        computer_card_shuffle()
        user_hand_status()
        print(f"Computer first card {computer_list[0]}")
        game_choice = input("Press 'y' to Draw another card and 'n' to Pass: ")
        if game_choice == 'n':
            computer_total = list_total(computer_list)
            user_total = list_total(user_list)
            


