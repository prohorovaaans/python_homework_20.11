#1 for
for i in range(1, 11):
    print(i)
#2 
for i in range(2, 51, 2):
    print(i)
#3
for i in range(10, 0, -1):
    print(i)
#4        
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
#5
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
#6
n = int(input())
for i in range(1, 11):
    print(n, i, n * i)
#7  
list = [5, -3, 8, 0, -2, 7, 4]
count = 0
for num in list:
    if num > 0:
        count += 1
print(count)
#8
text = input()
glas = "аеёиоуыэюя"
count = 0
for letter in text.lower():
    if letter in glas:
        count += 1
print(count)
#9
numbers = [12, 5, 27, 8, 19, 3]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)
#10
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()
    
#1 while  
i = 1
while i <= 10:
    print(i)
    i += 1
#2
total = 0
number = int(input())
while number != 0:
    total += number
    number = int(input())
print(total)
#3
n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)
#4
n = int(input())
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)
#5
n = int(input())
res = 0
while n > 0:
    d = n % 10
    res = res * 10 + d
    n //= 10
print(res)
#6
n = int(input())
power = 1
while power <= n:
    print(power)
    power *= 2
#7 
password = "12345"
user_password = input()
while user_password != password:
    print("Неверный пароль")
    user_password = input("Попробуйте ещё раз: ")
print("Пароль верный")
#8
a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print("Наибольший Общий Делитель:", a)
#9
n = int(input())
a = 0
b = 1
while a <= n:
    print(a)
    a, b = b, a + b
#10    
import random
secret = random.randint(1, 100)
attempts = 0
guess = int(input("Угадайте число: "))
while guess != secret:
    attempts += 1
    if guess < secret:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    guess = int(input("Попробуйте ещё раз: "))
attempts += 1
print("ура")
print("Количество попыток:", attempts)