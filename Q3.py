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
