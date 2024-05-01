# class Math:
#     def factorial(self, n):
#         if n == 0:
#             return 1
#         else:
#             return n * self.factorial(n-1)

#     def fibonacci(self, n):
#         if n <= 1:
#             return n
#         else:
#             return self.fibonacci(n-1) + self.fibonacci(n-2)

# # create an object of the Math class
# m = Math()

# # print the factorial of 5
# print("Factorial of 5:", m.factorial(5))

# # print the first 10 numbers in the fibonacci sequence
# print("Fibonacci sequence:", end=" ")
# for i in range(10):
#     print(m.fibonacci(i), end=" ")


# class math():
#     def fact(self,num):
#         if num==0 or num==1:
#             return 1
#         else:
#             return num*self.fact(num-1)
#     def fibo(self,num):
#         if num==0:
#             return 0
#         elif num==1:
#             return 1
#         else:
#             return  self.fibo(num-1)+ self.fibo(num-2)
#     def sum(self,num):
#         if num==0:
#             return 0
#         elif num==1:
#             return 1
#         else:
#             return num+self.sum(num-1)
        
        
# m=math()
# num=int(input())
# print(m.fact(num))

# for i in range(num+1):
#     print(m.fibo(i))

# print(m.sum(num))


# class math():
#     def hcf(self,a,b):
#         if a>b:
#             small=b
#         else:
#             small=a
#         for i in range(1,small+1):
#             if a%i==0 and b%i==0:
#                 hcf=i
#             return hcf
#     def factor(self,num):
#         for i in range(1,num+1):
#             if num%i==0:
#                 print(i)           
            
# m=math()
# a=int(input())
# b=int(input())
# print(m.hcf(a,b))

# num=int(input())
# print(m.factor(num))



# class math():
#     def palindrome(self,word):
#         reverse=word[::-1]
#         if reverse==word:
#             print("yes")
#         else:
#             print("no")
#     def armstrong(self,num):
#         n=len(str(num))
#         sum=0
#         for char in str(num):
#             sum+=int(char)**n
#             if sum==num:
#                 return True
#             else:
#                 return False

# m=math()
# word=str(input(""))
# print(m.palindrome(word))
# num=int(input())
# print(m.armstrong(num))


 #class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# # create objects of the Square and Circle classes
# square = Square(5)
# circle = Circle(3)

# # print the areas of the objects
# print("Area of square:", square.area())
# print("Area of circle:", circle.area())
# # In this example, we define a Shape class with one method, area(), which is defined as a pass statement. We also define two subclasses of Shape: Square and Circle. Each subclass overrides the area() method to calculate


# import math
# class cal():
#     def area(self,a):
#         return math.pi*a**2
# n=cal()
# a=int(input())
# print(n.area(a))

# class at():
#     def area(self,a,b):
#         return 1/2*(a*b)
# m=at()
# a=int(input())
# b=int(input())
# print(m.area(a,b))

