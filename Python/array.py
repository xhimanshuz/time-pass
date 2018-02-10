size = int(raw_input("Enter Size of an Array \n>> "))
array = []
print("Input %d Data in Array" %size)
for i in range(size):
    n = int(raw_input(">> "))
    array.append(n)

for i in range(size):
    print(array[i])
    
print("Done...!")
