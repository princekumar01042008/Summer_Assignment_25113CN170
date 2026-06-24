# WAP to calculate sum of first n natural numbers.

n = int(input("Enter a number:"))
sum = 0
for i in range(1, 1+n):
    sum = sum + i
print("Sum of first", n, "natural numbers is:", sum)