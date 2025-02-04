from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser (plain_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text+=char
    print(f"Here's the {cipher_direction}d result: {end_text}\n")


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your massage: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26

    ceaser(plain_text=text,shift_amount=shift,cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_end = True
        print("Bye")