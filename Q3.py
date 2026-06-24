<<<<<<< HEAD
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
=======
<<<<<<< HEAD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
=======
# WAP to find factorial of a number.
n = int(input("Enter a number:"))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print("Factorial of", n, "is:", factorial)
>>>>>>> 18ee8c73681a1804f33fe94ba26c99d8790eb5b6
>>>>>>> 5303cd916be2a6ceb387b57a0c6e1e372ec223db
