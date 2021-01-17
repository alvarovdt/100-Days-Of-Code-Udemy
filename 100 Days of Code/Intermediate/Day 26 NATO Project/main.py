import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
nato = [nato_dict[letter] for letter in user_input]

print(nato)

# for letter in user_input:
#     print(nato_dict[letter])

