#OPEN FILE METHOD
#f=open("demo.txt","r","w","a")
#r for read file means only see the file
# f  is handler
#  w  write means we can make some change in file
#a append file both read and write

#print(f.read())



# f=open("demo.txt","r")
# print(f.readline())   # it read entire file line by line




# f1=open("demo1.txt","w")  # it will create a new file
# f1.write("this is a new file")


# f2=open("demo2.txt","w")
# f2.write("hello sir i am ankit chaubey\n i am totally focused in your class")



# f=open("demo.txt","r")
# for i in f:
#     f2.write(i)

#OPTIMIZATION MAKE OUR CODE FAST

# f=open("demo.txt")
# f.close()#for closing file

#exception -->>code will further even having error 

# try:
#     f=open("demo.txt")
# finally:
#     f.close()
    #this way we are making sure that  file is closed properly even if exception is raised thatcause the program flow to stop

# with open("demo.txt") as f:
#     f.read()
#     #your code goes here




# f=open("demo.txt","r")
# print(f.read(4))    # it will read char of file till given no. in f.read() 
# print(f.tell())  #tell what value i defined in f.read()

# f1=open("image.png","rb")
# f2=open("image_copy.png","wb")  # add b in last of r and w for images
# print(f.read())

# for i in f1:
#     f1.write(i)


# import os  # for remove file
# os.remove("image_copy.png")

# import os
# if os.path.exists("hello.txt"):
#     os.remove("hello.text")
# else:
#     print("file does not exist")





f=open("demo4.txt","w")
f.write("i am ankit chaubey son of mr. dhananjay chaubey")

f1=open("demo4.txt","w")
f1.write("belong to a middle class family")


f1=open("demo4.txt","r")
print(f1.read())
print(f1.readline())



