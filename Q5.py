
def sum_of_digits(num):
    return sum(int(digit) 
               for digit in str(abs(num)))


number = int(input("Enter a number :"))
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}") 