name = ["Shin", "Lim"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combo = ["Shin", "Lim", 1, 2, 3]

for item in combo:
    print(item)
    
numbers.append(10)
print(numbers)

numbers.insert(1,100)
print(numbers)

numbers.extend([300, 400, 25])
print(numbers)