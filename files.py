file = open("Hello.txt", "r")

numbers = file.readlines()
for number in numbers:
    print(number)

file.close()