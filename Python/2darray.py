#!/usr/bin/python3
size = int(input("Enter Size: "))
matrix = []

for i in range(size):
    row=[]
    for j in range(size):
        row.append(input(">> "))
    matrix.append(row)

print(matrix) 
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=" ")
    print()