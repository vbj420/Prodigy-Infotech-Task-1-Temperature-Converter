def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 9/5

def convert_temperature(value, unit):
    if unit == 'Celsius':
        return value, celsius_to_fahrenheit(value), celsius_to_kelvin(value), celsius_to_rankine(value)
    elif unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
        return celsius, value, celsius_to_kelvin(celsius), celsius_to_rankine(celsius)
    elif unit == 'Kelvin':
        celsius = value - 273.15
        return celsius, celsius_to_fahrenheit(celsius), value, celsius_to_rankine(celsius)
    elif unit == 'Rankine':
        celsius = (value - 491.67) * 5/9
        return celsius, celsius_to_fahrenheit(celsius), celsius_to_kelvin(celsius), value
    else:
        return None

def main():
    try:
        temperature = float(input("\n Enter the temperature value: "))
        unit = input("\n Enter the unit (Celsius, Fahrenheit, Kelvin, Rankine): ").capitalize()

        result = convert_temperature(temperature, unit)

        if result:
            print(f"\n {temperature} {unit} is equal to:")
            print(f" {result[0]:.2f} Celsius")
            print(f" {result[1]:.2f} Fahrenheit")
            print(f" {result[2]:.2f} Kelvin")
            print(f" {result[3]:.2f} Rankine\n\n")
        else:
            print("Invalid unit entered. Please choose from Celsius, Fahrenheit, Kelvin, Rankine.\n")

    except ValueError:
        print("Invalid temperature value entered. Please enter a valid number.\n")

if __name__ == "__main__":
    main()
