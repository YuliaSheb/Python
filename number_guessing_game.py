import random


def game(p, number_p):
    print(f"You have {p} attempts remaining to guess the number")
    t = True
    while t:
        if p > 0:
            choose_number = int(input("Make a guess : "))
            p -= 1
            if choose_number == number_p:
                print(f"You win! My number {number_p}")
                t = False
            else:
                if choose_number > number_p:
                    print(f"Too high.\nGuess again.\nYou have {p} attempts remaining to guess the number")
                else:
                    print(f"Too low.\nGuess again.\nYou have {p} attempts remaining to guess the number")
        else:
            print(f"You lose! My number {number_p}")
            t = False


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 101)
n = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if n == "hard":
    game(5, number)
else:
    game(10, number)