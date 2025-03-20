#  1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა, მაგალითად მომხმარებელმა 
# თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10
#     2) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს
#     3) შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულკს
#     4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი
#     5) შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის ახლანდელ ასაკს და ამჟამინდელ წელს, ასევე რამდენი ხანით სურს დროშ მოგზაურობა შემდეგ კი ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში
# დავალება 1: 
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add/subtract/multiply/divide): ")
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"
    
    print(f"Result: {result}")



# დავალება 2: 
def sum_of_list():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)



# დავალება 3: 
def average_of_list():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers) / len(numbers)



# დავალება 4:
def odd_or_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")



# დავალება 5:
def time_travel():
    current_age = int(input("Enter your current age: "))
    current_year = int(input("Enter the current year: "))
    travel_years = int(input("Enter how many years you want to travel: "))
    direction = input("Do you want to travel to the past or future? (past/future): ")
    
    if direction == "future":
        future_year = current_year + travel_years
        future_age = current_age + travel_years
    else:
        future_year = current_year - travel_years
        future_age = current_age - travel_years
    
    print(f"After time travel, it will be the year {future_year} and you will be {future_age} years old.")




# დავალება 6:
def add_one():
    number = int(input("Enter a number: "))
    result = number + 1
    print(f"Result: {result}")



# დავალება 7 
def awesome_check():
    num = float(input("Enter a number: "))
    return "Awesome!" if num > 10 else "Not awesome enough!"



# დავალება 8 
def smaller_digit():
    digit1 = int(input("Enter first digit: "))
    digit2 = int(input("Enter second digit: "))
    return min(digit1, digit2)



# დავალება 9 
def text_length():
    text = input("Enter some text: ")
    return len(text)



# დავალება 10 
def sum_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2


# დავალება 11 
def positive_or_negative():
    num = float(input("Enter a number: "))
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"



# დავალება 12 
def is_even():
    num = int(input("Enter a number: "))
    return num % 2 == 0



# დავალება 13 
def sum_plus_five():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2 + 5




# ფუნქციების გატესტვა
calculator()
print(f"Sum of list: {sum_of_list()}")
print(f"Average of list: {average_of_list()}")
odd_or_even()
time_travel()
add_one()
print(awesome_check())
print(smaller_digit())
print(text_length())
print(sum_two_numbers())
print(positive_or_negative())
print(is_even())
print(sum_plus_five())
