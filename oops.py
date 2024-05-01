#perimeter of rectangle
# class rectangle(object):
#     def _init_(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         return self.length*self.breadth
# a=rectangle()
class rectangle():
    def _init_(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
a=rectangle()
l=int(input())
b=int(input())
print(a.area(l,b))

# print(a.area())

# class math():
#     def gcd(self,a,b):
#         if b==0:
#             return a
#         else:
#             return self.gcd(b,a%b)
# n=math()
# print(n.gcd(4,6))

     