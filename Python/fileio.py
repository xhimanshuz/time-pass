#Read File Text and Print it on Python Console
from sys import argv
source, filename = argv
print("You are using %r" %source)
print("File %r have %r Bytes" %(filename, len(filename)))
print("Opening File...")
openfile = open(filename)
print("Reading File...")
print(openfile.read())
print("Closing File...")
openfile.close();
