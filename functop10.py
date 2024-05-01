# Write a Python function to find the maximum of two numbers.
# Write a Python function to find the sum of all the elements in a list.
# Write a Python function to check whether a given number is prime or not.
# Write a Python function to find the factorial of a given number.
# Write a Python function to check whether a given string is a palindrome or not.
# Write a Python function to count the number of vowels in a given string.
# Write a Python function to find the length of the longest word in a given sentence.
# Write a Python function to remove all the duplicates from a given list.
# Write a Python function to find the second largest number in a list.
# Write a Python function to convert a binary number to decimal.


# def max(a,b):
#     if a>b:
#         return a
#     elif a==b:
#         return 0
#     else:
#         return b
# a=int(input())
# b=int(input())
# print(max(a,b))


# def find_sum(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i
#     return total
# n=int(input())
# print(find_sum(n))
# To check whether a given number is prime or not:
# python
# Copy code
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def is_palindrome(string):
#     string = string.lower()
#     rev_string = string[::-1]
#     if string == rev_string:
#         return True
#     else:
#         return False

def count_vowels(string):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char in vowels:
            count += 1
    return count
print(count_vowels("education"))
# To find the length of the longest word in a given sentence:
# python
# Copy code
# def longest_word(sentence):
#     words = sentence.split()
#     max_length = 0
#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#     return max_length
# To remove all the duplicates from a given list:
# python
# Copy code
# def remove_duplicates(lett):
#     return list(set(lett))
# lett=input()
# print(remove_duplicates(lett))


# To find the second largest number in a list:
# python
# Copy code
# def second_largest(lst):
#     if len(lst) < 2:
#         return None
#     lst = list(set(lst))
#     max_num = max(lst)
#     lst.remove(max_num)
#     second_max = max(lst)
#     return second_max

# list1=[2,1,4,3,6,5]
# list1.sort()
# print(list1[-2])

# To convert a binary number to decimal:
# python
# Copy code
# def binary_to_decimal(binary):
#     decimal = 0
#     binary = str(binary)
#     binary = binary[::-1]
#     for i in range(len(binary)):
#         if binary[i] == '1':
#             decimal += 2**i
#     return decimal



# def count_vowel(x):
#     for i in range(x):
#         if "aeiouAEIOU" in i:
#             print(i)
# print(count_vowel('orange'))


