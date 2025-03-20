# Initial list of car names, including some not-so-favorite ones
cars = ["Ferrari", "Toyota", "Porsche", "Fiat", "Lamborghini", "Kia", "Aston Martin", "Lada"]

# Replace the not-so-favorite cars with preferred ones
cars[1] = "McLaren"
cars[3] = "Bugatti"
cars[5] = "Koenigsegg"
cars[7] = "Pagani"

# Print the modified list in a single sentence
print("My favorite cars are: " + ", ".join(cars[:-1]) + ", and " + cars[-1] + ".")
