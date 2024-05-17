def add(x,y):
    result = x + y
    return result

def sum(*numbers):
    total = 0
    for number in numbers:
        total += numbers
    return total     


def subtract(x,y):
    result = x - y
    return result 

def divide(x,y):
    result = x / y
    return result 

def multiply(x,y):
    result = x * y
    return result 

def multiply_many(*nums):
    total = 1
    for num in nums:
        total *= num
    return total    

def remainder(x,y):
    result = x % y
    return result 

def power_of(x,y):
    result = x ** y
    return result 