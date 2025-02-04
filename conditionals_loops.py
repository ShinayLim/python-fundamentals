age = int(input("How old are you? "))

if age > 18:
    print("You are an adult")
else:
    print("You are a child")

num = 0 

while num < 10:
    print(num)
    num = num + 1
    
#Guessing game 

secret_number = 5 

guess = int(input("Enter your guess number: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
        
print("Congratulations! You have guessed the number")