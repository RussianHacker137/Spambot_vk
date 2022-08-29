text = input("Введите текст для спама: ")
with open('spam.txt', 'w') as file:
    for x in range(1000):
        file.write(text + " ")