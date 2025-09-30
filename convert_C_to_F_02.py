# Name: Justin Coon
# Date: 09-29-2025
# Description: A program that converts celcius to fahrenheit and vice versa

# Prints a banner
print("===== Temperature Converter =====\n")

# Prints the menu options
print("1. Convert from Celsius to Fahrenheit")
print("2. Convert from Fahrenheit to Celsius\n")

# Variable declaration for the menu choice and temperature to be converted
user_choice = int(input("Please choose from the above menu: "))

temperature = float(input("Enter a temperature to convert: "))


# Variable declaration for converting Fahrenheit to Celsius and vice versa
celsius = (temperature - 32 ) * 5/9

fahrenheit = temperature * 9/5 + 32


# If statement to check if menu option 1 was selected and prints degrees Celsius to degrees Fahrenheit
if user_choice == 1:
    
    print(f"\n{temperature} degrees Celsius is {fahrenheit} degrees Fahrenheit")

# Elif clause that checks if menu option 2 was chosen and prints degrees Fahrenheit to degrees Celsius    
elif user_choice == 2:
    
   print(f"\n{temperature} degrees Fahrenheit is {celsius} degrees Fahrenheit")