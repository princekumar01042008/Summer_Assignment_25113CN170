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