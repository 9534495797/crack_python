# string=input()
# vowel=0
# const=0
# for char in string:
#     if char.lower() in 'aeiou' or char.upper()in 'AEIOU':
#         vowel+=1
#     elif char.isalpha():
#         const+=1
# print(vowel)
# print(const)
string=input()
vowel=0
const=0
for char in string:
    if char in "aeiou" or char in "AEIOU":
        vowel+=1
    elif char.isalpha():
        const+=1
    else:
        print("wrong input")
print(vowel)
print(const)

# string=input("")
# vowe_count=0
# const_count=0
# for char in string:
#     if char.lower() in "aeiou":
#         vowe_count+=1
#     elif char.isalpha():
#         const_count+=1
# print(vowe_count)
# print(const_count)

# string=input("")
# vowel=0
# const=0
# for char in string:
#     if char.lower() in "aeiou":
#         vowel+=1
#     elif char.isalpha():
#         const+=1
# print(vowel)
# print(const)

# string=input()
# vowe_c=0
# const_c=0
# for char in string:
#     if   char.lower() in "aeiou":



