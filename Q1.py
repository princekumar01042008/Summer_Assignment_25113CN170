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
