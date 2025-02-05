file = open("Hello.txt", "r")

numbers = file.readlines()
print(numbers)

file.close()