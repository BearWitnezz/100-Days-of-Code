# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

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
