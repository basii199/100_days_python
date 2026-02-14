import pandas as pd
#TODO 1. Create a dictionary in this format:
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pd.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input('Enter a word. ').upper()
print([data_dict[letter] for letter in user_input])