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