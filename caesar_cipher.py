def caesar(plain_text, shift_amount, direction_type):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            x = alphabet.index(letter)
            if direction_type == "encode":
                new_x = x + shift_amount
            else:
                new_x = x - shift_amount
            if new_x > len(alphabet) - 1:
                new_x = new_x - len(alphabet) - 1
                new_letter = alphabet[new_x]
            else:
                new_letter = alphabet[new_x]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

t = True
while t:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    tip = input("Type yes or no\n")
    if tip == "no":
        t = False
