# TODO 1: Import the logo from art and print it.

# TODO 2: Store the lowercase alphabet in a list, a through z.

# TODO 3: Define caesar(original_text, shift_amount, encode_or_decode) with a docstring. It encodes or decodes
#   by shifting letters, then prints the result.

# TODO 4: When the direction is "decode", multiply the shift by -1 once, before the letter loop.
#   Nudge: flipping the sign inside the loop reverses every other letter.

# TODO 5: Walk the message. A character that is not in the alphabet (a space, number, or symbol) is copied
#   unchanged.

# TODO 6: A letter's new index is its alphabet index plus the shift. Wrap with modulo the length of the alphabet,
#   then take the letter at that index.

# TODO 7: Print "Here is the {direction}d result: " and the finished text.

# TODO 8: Loop while the user wants another run. Ask for encode or decode, the message, and the shift number.
#   Lowercase the direction and the message. Pass all three into caesar by keyword.

# TODO 9: Ask whether to go again: "Type 'yes' if you want to restart, 'no' if you want to continue:".
#   "yes" keeps the loop going. "no" stops it.

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    """Encode or decode a message by shifting its letters."""
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

reset = True
while reset:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to restart, 'no' if you want to continue:\n").lower()
    if restart == "yes":
        reset = True
    elif restart == "no":
        reset = False
