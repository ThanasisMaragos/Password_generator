import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["!","@","#","$","%","^","&","*","(",")"]
flag = False
while flag == False:
    x = int(input("Give us the length of the password: "))
    n_characters = int(input("Give us the number of characters: "))
    n_numbers = int(input("Give the number of numbers: "))
    n_symbols = int(input("Give us the number of symblols: "))
    total = n_symbols+n_characters+n_numbers
    if total == x:
        flag = True
    else:
        print("Make sure that the password length is equal to the sum of all the other characters")

password = []

c=""
for j in range(1,1+n_characters):
    c += random.choice(characters)
    password.append(c)
    c=""
print(password)

for t in range(1,1+n_numbers):
    c += str(random.randint(1,9))
    password.append(c)
    c = ""

print(password)
for j in range(1,1+n_symbols):
    c += random.choice(symbols)
    password.append(c)
    c = ""

print(password)
random.shuffle(password)
final_password = ''.join(map(str, password))
print("Your password is: ", final_password)