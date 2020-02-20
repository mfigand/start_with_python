# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator

def calcutate(first, second, operation):
    if  operation.lower() == 'add':
      result = first + second
    elif operation.lower() == 'substract':
      result = first - second
    else:
      result = 'Operation, not supported'
    return result

first = float(input('Enter first number: '))
second = float(input('Enter second number: '))
operation = input('Enter operation type (add or substract): ')

print(calcutate(first, second, operation))
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

