import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    card = sum(cards)
    return card


def compare(users_score, computers_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


end = True
while end:
    end_while1 = True
    end_while2 = True
    print(logo)
    computer_card = []
    user_card = []
    for i in range(2):
        computer_card.append(deal_card())
        user_card.append(deal_card())
    user_score = calculate(user_card)
    computer_score = calculate(computer_card)
    print(f"Your card: {user_card}")
    print(f"Summa = {user_score}")
    print(f"Diler's first card: {computer_card[0]}")
    while end_while1:
        if computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate(computer_card)
        else:
            end_while1 = False
    while end_while2:
        n = input("Do you want take card? ""y"" or ""n""\n")
        if n == "n":
            print(f"   Your final hand: {user_card}, final score: {user_score}")
            print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
            print(compare(user_score, computer_score))
            end_while2 = False
        else:
            user_card.append(deal_card())
            user_score = sum(user_card)
            print(f"Your card {user_card}, your sum = {user_score}")
    k = input("Do you want play? ""y"" or ""n""\n")
    if k == "n":
        end = False
