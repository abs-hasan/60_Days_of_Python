# Saving name in a list


guest_name = []

#del name

with open("./Input/Names/invited_names.txt") as file:
    name = file.readlines()
    for value in name:
        name = value.strip()
        guest_name.append(name)


# letter sample
with open("./Input/Letters/starting_letter.txt") as file:
    data = file.read()
    for names in guest_name:
        final_letter = data.replace("[name]",names)
        with open(f"./Output/ReadyToSend/letter_for_{names}.txt", mode = "a") as cl:
            cl.write(final_letter)