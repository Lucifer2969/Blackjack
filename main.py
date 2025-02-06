import random

def deal_card():
    """This function returns a random card to the list"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(list):
    """This function calculates the sum of the given list and checks the condition of BLACKJACK"""
    if sum(list) == 21 and len(list) == 2:
        return 0
    
    if 11 in list and len(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(u_score,c_score):
    """Compares the user and computer score and return the results."""
    if u_score == c_score:
        return "Draw😓"
    elif c_score == 0:
        return "You loose😒, Computer has a BLACKJACK"
    elif u_score == 0:
        return "You win, With a BLACKJACK👌"
    elif u_score > 21:
        return "You went over 21, You loose😒"
    elif u_score > 21:
        return "Opponent went over 21, You Win😊"
    elif u_score > c_score:
        return "You win😊"
    else:
        return "You loose😂"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print (f"Your card {user_cards}, Your Score {user_score}")
        print (f"Computer first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' if you want another card, 'n' if you want to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, your final score {user_score}")
    print(f"Computer final hand is {computer_cards}, computer final score {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play the game of BLACKJACK, type 'y' or 'n': ") == 'y':
    print('\n'*20)
    play_game()