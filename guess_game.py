words1 = ["python", "java", "kotlin", "javascript"]
words2 = ["apple", "banana", "cherry", "orange"]
words3= ["car", "bike", "train", "plane"]
# kategori seçimi
choose = input("Choose a category (1: Programming Languages, 2: Fruits, 3: Vehicles): ")

if choose == "1":
    # büyük küçük harf karışıklığı için
    choose = choose.lower()
    # kelime karıştırma ve seçme
    import random

    word = random.choice(words1)
    clue = word[0] + "_" * (len(word) - 1)
elif choose == "2":
    import random
    word = random.choice(words2)
    clue = word[0] + "_" * (len(word) - 1)
elif choose == "3":
    import random
    word = random.choice(words3)
    clue = word[0] + "_" * (len(word) - 1) 
else:
    print("Invalid category")
    exit()


clue = word[0] + "_" * (len(word) - 1)
print("Here is your first clue:", clue)
# hak veriyoruz
attempts = 3
while attempts > 0:
    guess = input("enter your first guess: ")
    if guess == word:
        print("Congratulations! You guessed the word.")
        break
    else:
          #clue yu sıfırla ve yeni ipucu oluştur
          clue = ""
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            clue += word[i]
        else:
            clue += "_"
    print("Here your clue:", clue)

    # hak azaltma
    attempts -= 1
    if attempts == 0:
        print("sorry, you have no more attempts left. The word was:", word)
        break
 
    guess = input("Enter your next guess: ")
    if guess == word:
            print("Congratulations! You guessed the word.")
            break
    else:
            attempts -= 1
            if attempts == 0:
                print("sorry, you have no more attempts left. The word was:", word)

    guess = input("Enter your next guess: ")
    if guess == word:
            print("Congratulations! You guessed the word.")
            break
    else:
            attempts -= 1
            if attempts == 0:
                print("sorry, you have no more attempts left. The word was:", word)
