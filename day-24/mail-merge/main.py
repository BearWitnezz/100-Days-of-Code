# TODO 1: Open input/Letters/starting_letter.txt with a relative path and read the whole letter into a variable.
# TODO 2: Open input/Names/invited_names.txt and get the names as a list. Check the hint docs: which method gives you
#  each line?
# TODO 3: Loop through the names. Each name may carry extra stuff at the end (look closely). Which string method cleans
#  that off?
# TODO 4: In each pass, swap the [name] placeholder in the letter for the clean name. Which string method replaces text?
# TODO 5: Save each new letter into Output/ReadyToSend/ as letter_for_<name>.txt. Which mode creates a new file?
# TODO 6: Run it and open one letter. Does it match the example, with no extra space before the comma?

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_file = open("./Input/Letters/starting_letter.txt")
letter = letter_file.read()
print(letter)
letter_file.close()

names = open("./Input/Names/invited_names.txt")
names_list = names.readlines()
for name in names_list:
    clean_name = name.strip()
    new_letter = letter.replace("[name]",clean_name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt","w") as file:
        file.write(new_letter)
names.close()
