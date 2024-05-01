# # Get user input
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # # Define function to find gcd using Euclidean algorithm
# def gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1 % num2)

# # Call the function and print the result
# result = gcd(num1, num2)
# print("The GCD of", num1, "and", num2, "is:", result)

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(4,8))

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(3,4))



# def hcf(a,b):
#     if b==0:
#         return a
#     else:
#         return hcf(b,a%b)
    
# print(hcf(4,7))


# find hcf of 4,8
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
a=int(input())
b=int(input())
print(hcf(a,b))