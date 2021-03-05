PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as guest_names:
    list_of_names = guest_names.readlines()

with open("./Input/Letters/starting_letter.docx") as letter:
    starting_letter = letter.read()
    for names in list_of_names:
        name = names.strip()
        output_letter = starting_letter.replace(PLACEHOLDER, name)
        print(output_letter)
        with open(f"Output/ReadyToSend/letter_for_{name}.docx",mode="w") as out:
            out.write(output_letter)