# Basic Calculator
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide_FREE(a, b):
    return a/b

def remainder(a, b):
    return a//b

def say_hello(a, b):
    print("hello")

def get_sum_ver1(n):
    return (n(n+1))/2

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)