alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reset = True
def caesar(message, shift_number, encode_or_decode):
    coded_message = ""
    if encode_or_decode == 'encode':
        for position in message:
            if position in alphabet:
                new_position = (alphabet.index(position) + shift_number) % 26
                coded_message += alphabet[new_position]
            else:
                coded_message += position
        print(coded_message)
    if encode_or_decode == 'decode':
        for position in message:
            if position in alphabet:
                new_position = (alphabet.index(position) - shift_number) % 26
                coded_message += alphabet[new_position]
            else:
                coded_message += position
        print(coded_message)
print("Welcome to the Secret Work Order Code!")
while reset:
    encode_or_decode = input("Encode or Decode?\n").lower()
    if encode_or_decode != 'encode' and encode_or_decode != 'decode':
        print("Invalid input. Please try again.")
    else:
        message = input("Enter your message:\n").lower()
        shift_number = int(input("Enter your shift number:\n"))
        caesar(message, shift_number, encode_or_decode)
        again = input("Do you want to continue? (y/n)\n").lower()
        if again == "n":
            reset = False
