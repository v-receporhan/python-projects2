import random
password_list =[]

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
numbers = [chr(i) for i in range(ord('0'), ord('9') + 1)]
symbol = [".","_"]

wish1 = int(input("How many letters of password do you want? : "))
wish2 = int(input("how many numbers of password do you want to:"))
wish3 = int(input("how many symbols of password do you want to:"))

for i in range(wish1):
    choose1 = random.choice(letters)
    password_list.append(choose1)


for i in range(wish2):
    choose2 = random.choice(numbers)
    password_list.append(choose2)

for i in range(wish3):
    choose3 = random.choice(symbol)
    password_list.append(choose3)



random.shuffle(password_list)

result = "".join(password_list)

print(result)