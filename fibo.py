# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return(fibo(num-1)+fibo(num-2))    
# num=int(input())
# for i in range(num):
#     print(fibo(i))



# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)
    
# n=int(input())
# for i in range(n):
#     print(fibo(i))


# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return (fibo(num-1)+fibo(num-2))
    
# num=int(input())
# for i in range(num):
#     print(fibo(i))

# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)
# num=int(input())
# for i in range(num+1):
#     print(fibo(i))

# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)
    
# num=int(input())
# for i in range(num+1):
#     print(fibo(i))


# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)
    
# num=int(input())
# for i in range(0,num+1):
#     print(i)

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
num=int(input())
for i in range(0,num):
    print(fibo(i))