# Python credit card validator program
# https://youtu.be/4wGuB3oAKc4
# 1. remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left
#   if result is a two digit number,
# add the two-digit number together to get a single digit
# Sum the totals of steps 2 and 3
# 5. If sum is divisble by 10, the credit card # is valid


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", " ")
card_number = card_number.replace(" ", "")
# reverse the string
card_number = card_number[::-1]

print(card_number)

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)


# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits


# step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
