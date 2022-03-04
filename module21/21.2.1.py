def factorial(number):
    if number == 1:
        return 1
    else:
        temp = factorial(number - 1)
        return number * temp


print(factorial(5))
