import pandas as pd

data = pd.read_csv("Data/nato_phonetic_alphabet.csv")


message = input("Enter a Name: ").upper()
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
result = [new_dict[value] for value in message]
print(result)

