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
