import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    user_input = input('Enter a word. ').upper()
    try:
        print([data_dict[letter] for letter in user_input])
    except KeyError:
        print('Use alphabets only')
    else:
        break
