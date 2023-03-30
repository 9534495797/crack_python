# def pali(x):
#  y=x[::-1]
#  if y==x:
#     return True
#  else:
#    return False
# x=input()
# print(pali(x))

def pali(word):
    inverse=word[::-1]
    if inverse==word:
        print("yes")
    else:
        print("no")
word=input()
print(pali(word))