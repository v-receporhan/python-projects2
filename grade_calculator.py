# ders sayısı sormak

subjects = int(input("how many lessons do you have? "))

# en az 4 ders olması için

if subjects > 4 or subjects < 0:
    print("invalid number of lessons")
    exit()

for i in range(subjects):
    # her dersin notunu sormak
    grade1= input(f"{i + 1}. Enter the grade for the 1st lesson: ")
    grade1= float(grade1)

    grade2 = input(f"{i + 1}. Enter the grade for the 2nd lesson: ")
    grade2 = float(grade2)

    grade3 = input(f"{i + 1}. Enter the grade for the 3rd lesson: ")
    grade3 = float(grade3)

    grade4 = input(f"{i + 1}. Enter the grade for the 4th lesson: ")
    grade4 = float(grade4)
# notların geçerli olup olmadığını kontrol etmek için
    if grade1 > 100 or grade2 > 100 or grade3 > 100 or grade4 > 100 or grade1 < 0 or grade2 < 0 or grade3 < 0 or grade4 < 0:
        print("invalid grade")
        break
    
    your_grade = (grade1 + grade2 + grade3 + grade4) / 4
    
    if your_grade <= 50:
        print("you have passed the lesson")
    
    elif your_grade >=85:
        print("you have passed the lesson with good grade")


    elif your_grade ==95:
        print("you have passed the lesson with perfect grade")
    elif your_grade  >= 50:
        print("you have failed the lesson")



    elif your_grade <= 101:
        print("invalid grade")
    # notu değerlendirmek

