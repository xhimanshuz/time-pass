#!/bin/python2.7
from sys import argv
def arm(n):
    an = n
    a = 0
    while(n!=0):
        r = n%10
        a = a + (r*r*r)
        n/=10
    if(an == a):
        print("Armstrong")
    else:
        print("Not Armstrong")
    pass
if(len(argv)>1):
    sourcefile, n = argv
    n = int(n)
    arm(n)
else:
    print("Enter Number: ")
    n = int(raw_input(">> "))
    arm(n)
