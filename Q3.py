# Program to Check Armstrong number
# An Armstrong number equals the sum of its own digits 
# each raised to the power of the number of digits

num = int(input("Enter a number: "))

temp = num
num_digits = len(str(num))  # count digits
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** num_digits  # add digit raised to power
    temp //= 10

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")