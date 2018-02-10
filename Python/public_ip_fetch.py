from urllib import urlopen
from sys import argv
def write_file(filename):
    filename += ".txt" 
    print("Opening File...!!")
    file = open(filename, "w+")
    print("Writing file...!")
    file.write("Your Public ip: " + urlopen("http://icanhazip.com").readline())
    file.close()
    print("Done...!")
    pass

def main():
    if(len(argv)==2):
        sourcefile, filename = argv
        #filename = str(filename)
        write_file(filename)
    else:
        filename = raw_input("Enter Filename: \n>>")
        write_file(filename)

main()
