character=input("")
vowels="aeiouAEIOU"
for char in character:
    if char.lower() in vowels:
        print("vowel")
    elif char.isalpha():
        print("consonant")
    else:
        print("not a letter")