from sys import argv

def table(n):
    for i in range(1, 11):
        print("%d X %d = %d" %(n, i, (i*n)))


if(len(argv)==2):
    sourcefile, n = argv
    n = int(n)
    table(n)
else:
    print("Enter Number: ")
    n = int(raw_input(">> "))
    table(n)
