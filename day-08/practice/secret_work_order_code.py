# TODO 1: Define caesar() to encode or decode a work order.
# TODO 2: Shift only letters, wrap around the alphabet, and reject a direction that is neither.
# TODO 3: Keep asking for another message until the user says no.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message_done = False
def caesar(message, shift_amount, encode_or_decode):
    """Encode or decode a work order and print the result."""
    encoded_message = ""
    if encode_or_decode != "encode" and encode_or_decode != "decode":
        print("Invalid input!")
    else:
        if encode_or_decode == "encode":
            for letter in message:
                if letter in alphabet:
                    new_position = (alphabet.index(letter) + shift_amount) % 26
                    new_message = alphabet[new_position]
                    encoded_message += new_message
                else:
                    encoded_message += letter
            print(f"Your coded work order: {encoded_message}.")
        elif encode_or_decode == "decode":
            shift_amount = shift_amount * -1
            for letter in message:
                if letter in alphabet:
                    new_position = (alphabet.index(letter) + shift_amount) % 26
                    new_message = alphabet[new_position]
                    encoded_message += new_message
                else:
                    encoded_message += letter
            print(f"Your coded work order: {encoded_message}.")
while not message_done:
    encode_or_decode = input("Encode or Decode?\n").lower()
    message = input("Message?\n").lower()
    shift_amount = int(input("Shift Number?\n"))
    caesar(message, shift_amount, encode_or_decode)
    again = input("Go again? yes or no?\n").lower()
    if again == "no":
        message_done = True
