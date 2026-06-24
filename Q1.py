<<<<<<< HEAD
# Program to Generate Fibonacci series

n = int(input("Enter number of terms: "))

a, b = 0, 1  # first two terms of Fibonacci series
print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  # update terms

print()
=======
<<<<<<< HEAD
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
=======
# WAP to calculate sum of first n natural numbers.

n = int(input("Enter a number:"))
sum = 0
for i in range(1, 1+n):
    sum = sum + i
print("Sum of first", n, "natural numbers is:", sum)
>>>>>>> 18ee8c73681a1804f33fe94ba26c99d8790eb5b6
>>>>>>> 5303cd916be2a6ceb387b57a0c6e1e372ec223db
