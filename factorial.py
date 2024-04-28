# def fact(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*fact(num-1)
# num=int(input())
# print(fact(num))

num=int(input())
if num==0 or num==1:
    print("1")
else:
    # for i in range(num,1):
        # print(i*(i-1))
        # i-=1
      print(num*(num-1)*(num-2))
