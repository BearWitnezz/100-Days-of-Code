# TODO 1: Store the lowercase alphabet, a through z. Start a reset flag at True.

# TODO 2: Define caesar(message, shift_number, encode_or_decode) with a docstring. Encode shifts forward. Decode
#   shifts backward.

# TODO 3: Encode walks the message. A letter's new index is (its alphabet index + the shift) modulo 26. Any other
#   character stays as it is. Print the coded message.

# TODO 4: Decode does the same walk, with (index - shift) modulo 26.

# TODO 5: Print "Welcome to the Secret Work Order Code!".

# TODO 6: Loop while reset is True. Ask "Encode or Decode?" and lowercase the answer.

# TODO 7: If the direction is neither "encode" nor "decode", print "Invalid input. Please try again." and do not
#   ask for a message.

# TODO 8: Otherwise ask for the message and the shift number. Lowercase the message, turn the shift into an int,
#   and call caesar.

# TODO 9: Then ask "Do you want to continue? (y/n)". "n" sets reset to False.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reset = True
def caesar(message, shift_number, encode_or_decode):
    """Shift a message forward to encode it or backward to decode it."""
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
