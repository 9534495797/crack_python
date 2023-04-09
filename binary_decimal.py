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
# binary=input()
# print(binary_to_decimal(binary))

#input 1011 out 11


# def btc(binary):
#     decimal=0
#     binary=str(binary)
#     binary=binary[::-1]
#     for i in range (len(binary)):
#         if binary[i]=='1':
#             decimal+=2**i
#     return decimal
# print(btc(1011))

def btd(num):
    decimal=0
    num=str(num)
    num=num[::-1]
    for i in range(len(num)):
        if num[i]=='1':
            decimal+=2**i
    return decimal
print(btd(1011))