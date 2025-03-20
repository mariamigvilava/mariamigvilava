# დავალება 1: Names List
names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("Names list:", names)

# დავალება 2: Even and Odd Numbers
even_numbers = []
odd_numbers = []

number = int(input("Enter a number: "))
if number % 2 == 0:
    even_numbers.append(number)
else:
    odd_numbers.append(number)

print("Even numbers list:", even_numbers)
print("Odd numbers list:", odd_numbers)
