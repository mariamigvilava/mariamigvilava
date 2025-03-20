# Example 1: Basic input and output
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example 2: Simple arithmetic
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# Example 3: String manipulation
word = input("Enter a word: ")
print(f"The word '{word}' has {len(word)} letters")

# Example 4: Conditional statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 5: Simple loop
for i in range(5):
    print(f"This is iteration {i+1}")
