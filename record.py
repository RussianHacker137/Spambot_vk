text = input("Enter the spam text: ")
with open('spam.txt', 'w') as file:
    for x in range(4096):
        file.write(text + " ")
