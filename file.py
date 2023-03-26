# f=open("demo.txt","r","w","a")\

# f=open("demo.txt","w")
# f.write("i am king kohli")
# f.write("this is a boy")
# #print(f.readlines()

#print(f.tell())
# import os
# os.remove("demo.txt")
# f=open("demo1.txt","r")
# print(f.readlines())
# print(f.tell())
# f=open("ab.jpg","rb")
# print(f.readlines())





# fo=open("hp.txt","w")
# fo.write("Harry Potter")
# fo.write("There is a difference in all harry potter books\nWe can see it as harry grows\nthe books were written by J.K rowling ")
# fo.close()

# fo=open('hp.txt','r')
# fi=open('writehp.txt','w')
# l=fo.readlines()
# for i in l:
#     if 'a' in i:
#         i=i.replace('a','')
#         fi.write(i)
# fi.close()
# fo.close()



# f=open("demo2.txt","w")
# f.write("myself ankit chaubey from gopakganj  bqvkjwvbrkj bjdjqeif   zdfjbekjfhiuwf   ajb")
# f=open("demo2.txt","r")
# f1=open("demo3.txt","w")
# l=f.readlines()
# for i in l:
#     if "a" in i:
#         i=i.replace('a','')
#         f1.write(i)




fileName = input("Enter the file to check: ").strip()

infile = open(fileName, "r")


vowels = set("A E I O U a e i o u")
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")

text = infile.read().split()


countV = 0
for V in text:
    if V in vowels:
        countV += 1

countC = 0
for C in text:
    if C in cons:
        countC += 1

print("The number of Vowels is: ",countV,"\nThe number of consonants is: ",countC)




