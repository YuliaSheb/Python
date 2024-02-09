import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr = nr_numbers+nr_symbols+nr_letters
str11 = []
str22 = []
str33 = []
str0 = []
for i in range(0, nr_symbols):
    str2 = random.choice(symbols)
    str22.append(str2)
for j in range(0, nr_numbers):
    str3 = random.choice(numbers)
    str33.append(str3)
for k in range(0, nr_letters):
    str1 = random.choice(letters)
    str11.append(str1)
i = 0
j = 0
k = 0
print(str11)
print(str22)
print(str33)
change = []
for q in range(0, nr_letters):
    change.append(1)
for q in range(0, nr_symbols):
    change.append(2)
for q in range(0, nr_numbers):
    change.append(3)
for s in range(0, nr):
    cont = random.choice(change)
    change.remove(cont)
    if cont == 1:
        if i > nr_letters-1:
            n = 1
            s -= n
            n += 1
        else:
            str0.append(str11[i])
            i += 1
    elif cont == 2:
        if j > nr_symbols-1:
            n = 1
            s -= n
            n += 1
        else:
            str0.append(str22[j])
            j += 1
    else:
        if k > nr_numbers-1:
            n = 1
            s -= n
            n += 1
        else:
            str0.append(str33[k])
            k += 1
print("".join(str0))


#Версия с курсов
#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")