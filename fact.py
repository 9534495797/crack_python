# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return(num*factorial(num-1))
# num=int(input(''))  
# print(factorial(num))


# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return (num*factorial(num-1))
    
# num=int(input())
# print(factorial(num))

# def func(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*func(num-1)
# print(func(6))

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input())
print(factorial(num))