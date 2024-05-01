# def is_armstrong(num):
#     # Count the number of digits
#     n = len(str(num))
#     sum = 0
#     for digit in str(num):
#         sum += int(digit)**n
#     if sum == num:
#         return True
#     else:
#         return False
# num=int(input())
# print(is_armstrong(num))

    
# class a():
#     def armstrong(num):
#         n=len(str(num))
#         sum=0
#         for char in str(num):
#             sum+=int(char)**n
#             if sum==num:
#                 return True
#             else:
#                 return False
# b=a()
# num=int(input())
# print(a.armstrong(num))

# def armstrong(num):
#     b=len(str(num))
#     sum=0
#     for char in str(num):
#         sum+=int(char)**b
#         if sum==num:
#             return True
#         else:
#             return False
# num=int(input())
# print(armstrong(num))

# def armstrong(num):
    
#     b=len(str(num))
#     sum=0
#     for char in str(num):
#         sum+=int(char)**b
#         if sum==num:
#             return True
#         else:
#             return False
# num=int(input())
# print(armstrong(num))

# def armstrong(num):
#     sum=0
#     b=len(str(num))
#     for i in str(num):
#         sum+=int(i)**b
#         if sum==num:
#             return True
#         else:
#             return False
# print(armstrong(20))

# def armstrong(num):
#     sum=0
#     b=len(str(num))
#     for i in str(num):
#         sum+=int(i)**b

#     if sum==num:
#         return True
#     else:
#         return False
# nuum=int(input())
# print(armstrong(nuum))

# def arm(num):
#     sum=0
#     b=len(str(num))
#     for i in str(num):
#         sum+=int(i)**b
#     if sum==num:
#         return True
#     else:
#         return False
# print(arm(6))

def arm(num):
    sum=0
    b=len(str(num))
    for i in str(num):
        sum+=int(i)**b
    if sum==num:
        return True
    else:
        return False
print(arm())

