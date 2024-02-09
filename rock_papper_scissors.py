import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose?")
n = input("Type 0 for rock, 1 for paper and 2 for scissors\n")
k = random.randint(0,2)
if n == "0":
    print(rock)
    if k == 0:
        print("Computer chose:")
        print(rock)
        print("Draw")
    elif k == 1:
        print("Computer chose:")
        print(paper)
        print("You lose!")
    elif k == 2:
        print("Computer chose:")
        print(scissors)
        print("You win!")
elif n == "1":
    print(paper)
    if k == 0:
        print("Computer chose:")
        print(rock)
        print("You win!")
    elif k == 1:
        print("Computer chose:")
        print(paper)
        print("Draw")
    elif k == 2:
        print("Computer chose:")
        print(scissors)
        print("You lose!")
elif n == "2":
    print(scissors)
    if k == 0:
        print("Computer chose:")
        print(rock)
        print("You lose!")
    elif k == 1:
        print("Computer chose:")
        print(paper)
        print("You win!")
    elif k == 2:
        print("Computer chose:")
        print(scissors)
        print("Draw")
else:
    print("Error")


