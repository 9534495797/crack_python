# x=int(input("num= "))
# y=x**0.5
# print(y)

#area of rect

# a=int(input("l= "))
# y=int(input("b="))
# z=a*y
# print("area=",z)



#swap two variables

# a=int(input("num1= "))
# y=int(input("num2="))
# temp=a
# a=y
# y=temp
# print("num1=",a)
# print("num2=",y)

#kg to pound
# x=int(input())
# y=x/0.453
# print(y)


#even odd
# x=int(input())
# if x%2==0:
#     print("even")
# else:
#     print("odd")

#largest between three

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print("a largest",a)
# elif b>a and b>c:
#     print("b is largest",b)
# else:
#     print("c is latrgest",c)

#leap year
x=int(input("l= "))
if (x%4)==0:
    if (x%100)==0:
        if (x%400)==0:
            print(x," year is leap",)
        else:
            print(x,"year is not leap")
    else:
        print(x,"leap year")
else:
    print(x,"year is not leap")