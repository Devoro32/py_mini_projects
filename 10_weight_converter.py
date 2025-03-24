
weight= float(input("Enter your weight: "))
unit= input('Kilograms or pounds? (K or L): ').lower()


if unit=='k':
    weight = weight * 2.205
    unit="Lbs."
    print(f"Your weight is: { round(weight,3)}{unit}")
elif unit == 'l':
    weight= weight/2.205
    unit="Kgs."
    print(f"Your weight is: { round(weight,3)}{unit}")
else:
    print(f"{unit} wa not valid")


