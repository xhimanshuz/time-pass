#Input Data by user in file
from sys import argv
from os.path import exists
source, filename = argv
print("Enter Data in %r" %filename)
print("Currently in %r \n" %filename)
ofile = open(filename, "r+w+")
print(ofile.read())
line1 = raw_input("Enter Text to Line 1: ")
line2 = raw_input("Enter Text to Line 2: ")
ofile.write(line1)
ofile.write(line2)
ofile = open(filename, "r")
print("Printing %r Text: \n " %filename)
print(ofile.read())
ofile.close()
