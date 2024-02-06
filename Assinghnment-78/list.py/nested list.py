

# n=3
# m=4
# matrix=[[]]*n
# for i in range(n):
#     for j in range (m):
#         k=int(input("enter the number"))
#         matrix [i].append(k)
#     print (matrix)

n=3
m=4
matrix=[[]]*n
for i in range(n):
    for j in range (m):
        k=int(input("enter the number"))
        matrix[i]=matrix[i]+[k]
print (matrix )