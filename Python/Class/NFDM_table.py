n=int(input("Enter N for N x N matrix : "))         #3 here
l=[]                                                #use list for storing 2D array

#get the user input and store it in list (here IN : 1 to 9)
for i in range(n):
  row_list=[]                                      #temporary list to store the row
  for j in range(n):
     row_list.append(int(input()))                 #add the input to row list
  l.append(row_list)                               #add the row to the list

print(l)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Display the 2D array
for i in range(n):
  for j in range(n):
    print(l[i][j], end=" ")
    print("[{}][{}]".format(i, j))
  print()
