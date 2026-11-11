# TODO 1: Store the lowercase alphabet, a through z. Start message_done as False.

# TODO 2: Define caesar(message, shift_amount, encode_or_decode) with a docstring. It encodes or decodes a work
#   order and prints the result.

# TODO 3: If the direction is neither "encode" nor "decode", print "Invalid input!" and skip the shift.

# TODO 4: For encode, walk the message. A letter's new index is (its alphabet index + the shift) modulo 26.
#   Anything that is not a letter is copied as-is. Print "Your coded work order: " and the result.

# TODO 5: For decode, multiply the shift by -1 first, then do that same walk and print the same sentence.

# TODO 6: Loop until message_done. Ask "Encode or Decode?", "Message?", and "Shift Number?". Lowercase the
#   direction and the message, turn the shift into an int, and pass all three to caesar.

# TODO 7: Ask "Go again? yes or no?". An answer of "no" sets message_done to True.

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
