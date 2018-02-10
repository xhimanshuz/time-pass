from sys import argv
source, filename = argv
print("Going to Erase File Data...! \n If want to stop then Press Ctrl+C")
print("Opening File...")
ofile = open(filename, "w")
ofile.truncate()
print("File Erased!")
ofile = open(filename, "r")
print(ofile.read())
print("Closing File...")
ofile.close()
