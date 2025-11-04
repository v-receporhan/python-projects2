import random

how_many = int(input("How many dice do you want to roll? "))

#sonsuz döngü.
while True:
    for i in range(how_many):
        
        #1 ile 6 arasında rastgele sayı üretiyor (zar atıyor).
        result = random.randint(1,6)
        print(f"{i+1}. zar: {result}")

    playagain = input("Do you want to roll again? (y/n): ")
    if playagain.lower() not in ['y', 'yes']:
        break
