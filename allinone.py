#i=0
#num=int(input())
#while i<=num:
    #print(i*"*")
    #i+=1
#def sum(num):
   # if num==0 or num==1:
        #return 1
   # else:
     #   return num+sum(num-1)
#num=int(input())
#print(sum(num))

#def palindrome(word):
    #reverse=word[::-1]
   # if word==reverse:
      #  print("yes")
    #else:
       # print("no")

#word=str(input())
#print(palindrome(word))

#def fact(num):
 #   for i in range(1,num+1):
  #      if num%i==0:
   #         print(i)
#print(fact(15))


#def fibo(num):
 #   if num==0:
  #      return 0
   # elif num==1:
    #    return 1
    #else:
        #return fibo(num-1)+fibo(num-2)
#num=int(input())
#for i in range(num):
  #  print(fibo(i))
#def hcf(a,b):
 #   if a>b:
  #      small=b
   # else:
    #    small=a
    #for i in range(1,small+1):
     #   if a%i==0 and b%i==0:
      #      hcf=i
       # return hcf
#a=int(input())
#b=int(input())
#print(hcf(a,b))


# def armstrong(num):
#     n=len(str(num))
#     sum=0
#     for char in str(num):
#         sum+=int(char)**n
#         if sum==num:
#             return True
#         else:
#             return False
           
# num=int(input())
# print(armstrong(num))


# num=int(input())
# i=num
# while i<=num*10:
#     print(i)
#     i+=num
