# https://youtu.be/4wGuB3oAKc4

principle = 0
rate = 0
time = 0


while True:
    principle = float(input(" Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break


while rate <= 0:
    rate = float(input(" Enter the interest amount: "))
    if rate < 0:
        print("Rate can't be less than zero")
    else:
        break


while time <= 0:
    time = int(input(" Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
