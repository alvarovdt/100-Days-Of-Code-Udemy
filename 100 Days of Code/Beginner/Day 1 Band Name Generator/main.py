#1. Create a greeting for your program.
print('Welcome to the Band Name Generator!')
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = "Your band name could be " + city + " " + pet_name
print(band_name)

#print("Your band name could be " + city + " " + pet_name)


print("With no variables...")
print("Your band name could be " + input("What's name of the city you grew up in?\n") + " " + input("What's your pet's name?\n"))
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/