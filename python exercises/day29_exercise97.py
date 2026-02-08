"""Temperature Analytics
a) Function to convert °C to °F
b) Function to classify temperature
c) Apply to a list of temperatures"""
import sys


def main():
    #define a function to convert °C to °F
    def temperature_conversion(celsius):
      fahrenheit = (celsius * 9 / 5) + 32
      return fahrenheit

    #define a function to classify temperature
    def classify_temperature(fahrenheit):
        if fahrenheit < 65:
            return "Cold"
        elif 65 <= fahrenheit <= 85:
            return "Normal"
        else:
            return "Hot"

    temperatures = []

    #ask the user to enter values of temperature
    try:
        for i in range(4):
            num = float(input("Enter temperature: "))
            temperatures.append(num)
    except ValueError:
        print("Enter a number")
        return 1

    print("The temperatures in celsius are: ", temperatures)
#test values are 1, 30, 60, 100
    temperature_in_fahrenheit = []
    for temp in temperatures:
        f = temperature_conversion(temp)
        temperature_in_fahrenheit.append(f)
        label = classify_temperature(f)
        print("The temperature in °F is: ", f)
        print("It is: ", label)

    print("The temperatures in fahrenheit are: ", temperature_in_fahrenheit)

    return 0

if __name__ == "__main__":
    sys.exit(main())
