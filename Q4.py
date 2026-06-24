<<<<<<< HEAD
# Program to Print Armstrong numbers in a range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end}:")

for num in range(start, end + 1):
    temp = num
    num_digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits  # sum of digits raised to power
        temp //= 10

    if total == num:
        print(num, end=" ")  # print if Armstrong number

print()
=======
<<<<<<< HEAD
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
=======
# WAP to count digits in a number.
n = int(input("Enter a number:"))
count_digits = len(str(n))
print("Number of digits in", n, "is:", count_digits)
>>>>>>> 18ee8c73681a1804f33fe94ba26c99d8790eb5b6
>>>>>>> 5303cd916be2a6ceb387b57a0c6e1e372ec223db
