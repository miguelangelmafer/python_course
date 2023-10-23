import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()


def generate_phonetic():
    try:
        output = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
