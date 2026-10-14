# Day 8: Caesar Cipher

Run `main.py` to encode or decode a message by shifting its letters. The ASCII logo is in `art.py`.

## Bugs I fixed along the way

- I moved the `shift_amount *= -1` decode flip above the for loop. Inside the loop, the sign flipped on every letter, so decoding "ab" by 3 gave "xe".
- Symbols, numbers, and spaces now pass through unchanged, thanks to an `if letter not in alphabet` check.
- A while loop lets you run the program again, with the `caesar()` call inside the loop.
