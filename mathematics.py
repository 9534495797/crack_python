# Write a program to find the roots of a quadratic equation.
# Write a program to find the sum of the first N natural numbers.
# Write a program to calculate the area of a circle given its radius.
# Write a program to find the greatest common divisor (GCD) of two numbers.
# Write a program to calculate the factorial of a number using recursion.
# Write a program to find the nth Fibonacci number.
# Write a program to generate a multiplication table up to a given number.
# Write a program to find the sum of digits of a given number.
# Write a program to check whether a given number is an Armstrong number or not.
# Write a program to calculate the sum of the series: 1 + 1/2 + 1/3 + ... + 1/N.
# import math
import math
def quadr(a,b,c):
    disc=(b*b)-4*a*c
    if disc>0:
        a=-b+(math.sqrt(disc))/2*a
        b= a=-b-(math.sqrt(disc))/2*a
        return a,b
    elif disc==0:
        root=-b/(2*a)
        return root
    else:
        return "imaginary roots"
a=int(input())
b=int(input())
c=int(input())
print(quadr(a,b,c))
# def quadratic_roots(a, b, c):
#     # Calculate the discriminant
#     disc = b**2 - 4*a*c

#     if disc > 0:
#         # Calculate the two real roots
#         root1 = (-b + math.sqrt(disc)) / (2*a)
#         root2 = (-b - math.sqrt(disc)) / (2*a)
#         return root1, root2
#     elif disc == 0:
#         # Calculate the one real root
#         root = -b / (2*a)
#         return root
#     else:
#         # Calculate the two imaginary roots
#         real = -b / (2*a)
#         imag = math.sqrt(-disc) / (2*a)
#         return (real, imag), (real, -imag)
# Program to find the sum of the first N natural numbers:
# python
# Copy code
# def sum_natural_numbers(n):
#     return sum(range(1, n+1))

# import math
# def area(r):

#     return math.pi*r*r
# r=int(input())
# print(area(1))


# Program to find the greatest common divisor (GCD) of two numbers:
# python
# Copy code
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# Program to calculate the factorial of a number using recursion:
# python
# Copy code
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# Program to find the nth Fibonacci number:
# python
# Copy code
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# Program to generate a multiplication table up to a given number:
# python
# Copy code
# def multiplication_table(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             print(i * j, end="\t")
# print(multiplication_table(10))
# Program to find the sum of digits of a given number:
# python
# Copy code
# def sum_digits(num):
#     total = 0
#     for digit in str(num):
#         total += int(digit)
#     return total
# Program to check whether a given number is an Armstrong number or not:
# python
# Copy code
# def is_armstrong(num):
#     # Count the number of digits
#     n = len(str(num))

#     # Calculate the sum of the nth powers of the digits
#     sum = 0
#     for digit in str(num):
#         sum += int(digit)**n

#     # Check if the sum equals the original number
#     if sum == num:
#         return True
#     else:
#         return False
# Program to calculate the sum of the series: 1 + 1/2 + 1/3 + ... + 1/N:
# python
# Copy code
# def series_sum(n):
#     total = 0
#     for i in range(1, n+1):
#         total += 1/i
#     return total


