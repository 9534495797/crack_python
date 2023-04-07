punc="",#@%^&*()??';';
str=input("")
no_punc=""
for char in str:
    if char not in punc:
        no_punc+=char
    print(no_punc)