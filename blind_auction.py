logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

clear = "\n"*95
print("Welcome to the auction")
auction = {}
t = True
while t:
    print(logo)
    name = input("Your name\n")
    money = int(input("How many money\n"))
    auction[name] = money
    change = input("Is there other person: yes or no\n")
    if change == "yes":
        print(clear)
        t = True
    else:
        print(clear)
        print(logo)
        t = False
maxn = 0
for key in auction:
    if auction[key] > maxn:
        maxn = auction[key]
        names = key
print(f"Max pay {names} is have {maxn}$")