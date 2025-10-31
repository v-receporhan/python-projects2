# 1.simple calculater
print("mini calculater")
# kullanıcıdan sayılar ve işlemler isteme kısmı

num1= input("choose a number")
num2= input("choose a number")

# floata çevirme

num1 = float(num1)
num2 = float(num2)

# işlem türü seçme

operation = input("choose an operation + - * /3333 : ")

if operation == '+':
    result = num1+ num2

elif operation == '-':
    result = num1-num2

elif operation == '*':
    result = num1*num2

elif operation == '/':
    result = num1/num2

# en son kısım hiçbiri olmazsa
else:
    result = "invalid operation"

print("Result:",result)