from sys import argv

def parm(n):
    for i in range(2,n):
        arm(i)

def arm(n):
    an = n
    arm = 0
    while n!=0:
        r = n%10
        arm = arm + (r*r*r)     #Armstrong Equation
        n/=10
    if(an == arm):
        print(arm)
    else:
        pass

if(len(argv)==2):               #If Argument then Executes
    sourcefile, n = argv
    parm(int(n))
else:
    print("Enter Range: ")    #Non Argument
    n = int(raw_input(">> "))
    parm(n)
