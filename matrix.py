# a=[[4,8],
#    [3,19],
#    [14,6]]
# trans=[[0,0,0],
#        [0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         trans[j][i]=a[i][j]
# for k in trans:
            
#             print(k)


# a=[[4,8],
#    [3,19],
#    [14,6]]
# b=[[4,8],
#    [3,19],
#    [14,6]]
# sum=[[0,0],
#      [0,0],
#      [0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         sum[i][j]=a[i][j]+b[i][j]
# for k in  sum:
#     print(k)


# # Initialize a 3x3 matrix with zeros
# matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# # Get user input to fill the matrix
# print("Enter values for a 3x3 matrix:")
# for i in range(3):
#     for j in range(3):
#         matrix[i][j] = int(input("Enter value for position [{},{}]: ".format(i, j)))

# # Print the original matrix
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Transpose the matrix
# transpose = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(3):
#     for j in range(3):
#         transpose[j][i] = matrix[i][j]

# # Print the transpose matrix
# print("Transpose Matrix:")
# for row in transpose:
#     print(row)


# a=[[1,2,3],
#    [2,3,4],
#    [3,4,5]]

# b=[[1,2,3],
#    [2,3,4],
#    [3,4,5]]
# sum=[[0,0,0],
#      [0,0,0],
#      [0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         sum[i][j]=a[i][j]+b[i][j]
# for k in sum:
#     print(k)



# a=[[1,2,3],
#    [2,3,4],
#    [3,4,5]]



# transpose=[[0,0,0],
#            [0,0,0],
#            [0,0,0]]
# for i in range(len(a)):
#     for j in range (len(a[0])):
#         transpose[j][i]=a[i][j]
# for k in transpose:
#     print(k)


matrix=[[0,0,0],[0,0,0],[0,0,0]]
print("write")
for i in range(3):
    for j in range(3):
        matrix[i][j]=int(input("enter value".format(i,j)))