<<<<<<< HEAD
# Program to Find nth Fibonacci term

n = int(input("Enter the value of n: "))

a, b = 0, 1  # first two terms

if n == 1:
    print(f"{n}th Fibonacci term is {a}")
elif n == 2:
    print(f"{n}th Fibonacci term is {b}")
else:
    for i in range(3, n + 1):
        a, b = b, a + b  # move to next term
    print(f"{n}th Fibonacci term is {b}")
=======
<<<<<<< HEAD
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
=======
# WAP to print multiplication table of a given number.

n = int(input("Enter a number:"))
for i in range(1, 11):  
    print(n, "x", i, "=", n*i)
>>>>>>> 18ee8c73681a1804f33fe94ba26c99d8790eb5b6
>>>>>>> 5303cd916be2a6ceb387b57a0c6e1e372ec223db
