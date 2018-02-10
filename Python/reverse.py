from sys import argv
rev = 0
if(len(argv) > 1):
    sourcefile, n = argv
    n = int(n)
else:
    print("Enter Number: ")
    n = int(raw_input(">> "))

while n!=0:
    r = n%10
    rev = rev * 10 + r
    n/=10
print("Reverse Number: %d " % rev)
