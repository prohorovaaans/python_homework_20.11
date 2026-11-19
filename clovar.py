#1
students = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
name = input("Введите имя: ")
print("Оценка:", students[name])
#2
students = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
students["Пётр"] = 5
students["Иван"] = 3
del students["Мария"]
print(students)
#3
students = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
key = input("Введите имя: ")
if key in students:
    print(students[key])
else:
    print("Нет такого ключа")
#4
students = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
print(students.keys(), students.values(), len(students))
#5
products = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 350,
    "Яблоки": 120
}
for product, price in products.items():
    print(product, price)
#6      
products = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 350,
    "Яблоки": 120
}
sum = 0
expensive_product = ""
max_price = 0
for product, price in products.items():
    sum += price
    if price > max_price:
        max_price = price
        expensive_product = product
print(sum, expensive_product)
#7
text = input()
symbols = {}
for char in text:
    if char in symbols:
        symbols[char] += 1
    else:
        symbols[char] = 1

print(symbols)
#8
text = "Hello Kitty in Russia Hello"
words = text.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
most_common = ""
max_count = 0
for word, amount in count.items():
    if amount > max_count:
        max_count = amount
        most_common = word
print("Количество слов:", count)
print("Самое частое слово:", most_common)
print("Количество повторений:", max_count)
#9
original = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
reversed_dict = {}
for key, value in original.items():
    reversed_dict[value] = key
print(reversed_dict)
#10
countries = ["Россия", "Франция", "Германия", "Италия"]
capitals = ["Москва", "Париж", "Берлин", "Рим"]
country_capitals = {}
for i in range(len(countries)):
    country_capitals[countries[i]] = capitals[i]
country = input("Введите страну: ")
if country in country_capitals:
    print("Столица:", country_capitals[country])
else:
    print("Такой страны нет в списке")