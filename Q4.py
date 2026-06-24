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
