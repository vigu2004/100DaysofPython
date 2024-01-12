import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# easy method
res=""

for i in range(0,nr_letters):
    res+= random.choice(letters)

for i in range(0,nr_symbols):
   res+= random.choice(symbols)

for i in range(0,nr_numbers):
     res+= random.choice(numbers)

print(res)

# hard method
res_list=[]

for i in range(0,nr_letters):
    res_list.append(random.choice(letters))

for i in range(0,nr_symbols):
   res_list.append(random.choice(symbols))

for i in range(0,nr_numbers):
     res_list.append(random.choice(numbers))

random.shuffle(res_list)
res_shuffled=""
for i in res_list:
    res_shuffled+=i
print(res_shuffled)