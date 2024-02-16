with open(file="input/Names/invited_names.txt") as t:
    names = t.readlines()

names_list = []
x = "[name]"
for i in names:
    ok = i.strip()
    names_list.append(ok)

with open("input/Letters/starting_letter.txt") as t:
    letter = t.read()

for names in names_list:
    with open(file=f"Output/ReadyToSend/{names}", mode="w") as t:
        new_letter = letter.replace("[name]", names)
        t.writelines(new_letter)