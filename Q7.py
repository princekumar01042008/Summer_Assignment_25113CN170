def product_of_digits(num):
   
    num_str = str(abs(num))
    
    product = 1
    for digit in num_str:
        product *= int(digit)
        
    return product
number =int(input("Enter a number:"))
result = product_of_digits(number)
print(f"The product of digits of {number} is: {result}")