# For loop with range
for i in range(5):
    print(f"Iteration {i}")


# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")




# Nested if/else
x = 10
y = 20
if x > 5:
    if y > 15:
        print("Both conditions are true")
    else:
        print("Only x > 5 is true")
else:
    print("x is not greater than 5")



# While loop with break
num = 0
while True:
    if num == 5:
        break
    print(num)
    num += 1


# For loop with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")