def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = int(input("Enter your choice (1/2/3/4/5/6): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {result}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result}°C")
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {result} K")
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K is equal to {result}°C")
    elif choice == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result} K")
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} K is equal to {result}°F")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
