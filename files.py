file = open("Hello.txt", "r")

numbers = file.readlines()
sum = 0 
for number in numbers:
    sum = sum + int(number.strip())
    
print(sum)

file.close()
