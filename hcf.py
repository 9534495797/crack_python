# def hcf(a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1,small+1):
#         if a%i==0 and b%i==0:
#             hcf=i
#     return hcf
# print(hcf(10,20))

# def hcf(a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1,small+1):
#         if a%i==0 and b%i==0:
#             hcf=i
#         return hcf
# a=int(input())
# b=int(input())
# print(hcf(a,b))
    
# def hcf(a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1,small+1):
#         if a%i==0 and b%i==0:
#             hcf=i
#         return hcf
# a=int(input())
# b=int(input())
# print(hcf(a,b))


# def hcf(a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1,small+1):
#        if a%i==0 and b%i==0:
#            hcf=i
#        return hcf
# a=int(input())
# b=int(input())
# print(hcf(a,b))

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
a=int(input())
b=int(input())
print(hcf(a,b))