# def leap(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 print("yes leap")
#             else:
#                 print("no leap")
#         else:
#             print("yes")
#     else:
#         print("no not")
# year=int(input())
# print(leap(year))

def leap(year):
    if year%4==0:
        if year%100==0:
            if year %400==0:
                print("yes")
            else:
                print("no")
        else:
            print("yes leap")
    else:
        print("no leap")
year=int(input())
print(leap(year))
        