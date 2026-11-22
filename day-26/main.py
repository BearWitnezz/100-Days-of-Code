import pandas

# TODO 1. Read nato_phonetic_alphabet.csv into a DataFrame.

# TODO 2. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
#         Use a dictionary comprehension that loops with .iterrows().

# TODO 3. Ask the user to type a word.

# TODO 4. Create a list of the phonetic code words for each letter in their word.

# TODO 5. Print the list.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Type a word: ").upper()
phonetic_code = [nato[letter] for letter in word]
print(phonetic_code)
