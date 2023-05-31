# class rectangle():
#     def _init_(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
# a=rectangle()
# l=int(input())
# b=int(input())
# print(a.area(l,b))
while True:
    a=int(input())
    if a%4==0:
       if a%100==0:
          if a%400==0:
            print("yes leap year")
          else:
            print("no leap year")
    else:
        print("leap year")
else:
    print("not leap year")


