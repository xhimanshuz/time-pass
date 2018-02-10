from sys import argv
from os.path import exists

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def fout(fname, lname, age):
    choice = str(raw_input("Want To write this on your file? y/n: "))
    if(choice == 'y'):
        filename = raw_input("Enter File name with Extension: \n >> ")
        print(O + "Checking File Exists..." + W )
        print("File Exists:" + R + " %r" % exists(filename))
        file = open(filename, "w")
        print("Writting on file...")
        file.write("""First Name: %r
Last Name: %r
Age: %r""" %(fname, lname, age))
        print("Writting Done...!")
        file.close()
    else:
        print("Not Write")

def out(fname, lname, age):
    print("============================")
    print("Your First Name is " + B + "%s" %fname)
    print(W + "Your Last Name is" + B + " %s" %lname)
    print(W + "You are " + B + str(age) + W + " yrs old Fucking Virgin")
    print("============================")
    fout(fname, lname, age)

def inp():
    fname = str(raw_input("Enter First Name:\n >> "))
    lname = str(raw_input("Enter Last Name:\n >> "))
    age = int(raw_input("Enter Age:\n >> "))
    return fname, lname, age


if(len(argv)==4):
    sourcefile, fname, lname, age = argv
    age = int(age)
    out(fname, lname, age)

else:
    fname, lname, age = inp()
    out(fname, lname, age)
