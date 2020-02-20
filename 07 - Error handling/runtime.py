x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print("Sorry, can't divide by zero")
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
