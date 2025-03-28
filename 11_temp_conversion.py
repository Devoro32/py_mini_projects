# https://youtu.be/4wGuB3oAKc4

unit = input("Is this tempature in Celsius or Fahrenheit (C/F): ?").lower()
temp = float(input("Enter the temperature: "))


if unit == "c":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "f":
    temp = round(((temp - 32) * (5 / 9)), 2)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")
