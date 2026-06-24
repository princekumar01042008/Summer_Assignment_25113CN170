
def reverse_number(num):
    # Check if the number is negative
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    
    return sign * reversed_num

number =int(input("Enter a number:"))
print(f"Original: {number}")
print(f"Reversed: {reverse_number(number)}")