def length_converter():
    print("Length Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print("Distance in miles:", miles)
    elif choice == 2:
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print("Distance in kilometers:", km)
    else:
        print("Invalid choice")


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice")


def weight_converter():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print("Weight in pounds:", pounds)
    elif choice == 2:
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print("Weight in kilograms:", kg)
    else:
        print("Invalid choice")


def main():
    print("Unit Converter")
    print("1. Length Converter")
    print("2. Temperature Converter")
    print("3. Weight Converter")
    option = int(input("Enter your choice: "))
    if option == 1:
        length_converter()
    elif option == 2:
        temperature_converter()
    elif option == 3:
        weight_converter()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
 