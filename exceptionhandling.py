#for making errors in code too less

#try:
    #this block of code will run and throw erors if there are any
#except:
    #if any error in try than except will handle it

#else:
    #this will execute if there are no errors
#finally:
#this will execute regardless the result of try and except








# try:

#     f= open("demo.py")
#     try:
#         f.write("abc")
#     except:
#         print("error in file")
#     finally:
#         f.close()
# except:
#     print("can't open file")





# a=5
# if a<10:
#     raise Exception("value is less than 5")


# a = [1, 2, 3]
# try: 
#     print ("Second element = %d" %(a[1]))
  
#     # Throws error since there are only 3 elements in array
#     print ("Fourth element = %d" %(a[3]))
  
# except:
#     print ("An error occurred")




# def fun(a):
#     if a < 4:
  
#         # throws ZeroDivisionError for a = 3
#         b = a/(a-3)
  
#     # throws NameError if a >= 4
#     print("Value of b = ", b)
      
# try:
#     fun(3)
#     fun(5)
  
# # note that braces () are necessary here for 
# # multiple exceptions
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")




 #Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)