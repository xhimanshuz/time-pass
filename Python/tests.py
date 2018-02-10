from sys import argv
import os.path
import os
#GLOBAL VARIABLE
file_opened = False
filename = ' '
ofile = ""
def openfile(filename):
    ofile = open(filename, 'w')
    file_opened = True
    return ofile

def exist_checking(filename):
    return os.path.isfile(filename)

def savefile(ofile, string):
    if file_opened is False:
        openfile(filename)
    ofile.write(string)
    return ofile

def exiting(string, ofile):
    ch = input("Do you want to Save File: (y/n)")
    if ch is 'y' or ch is 'Y':
        ofile = savefile(ofile, string)
    ofile.close()

    exit()

def enter_filename():
    filename = str(input("File Name: "))
    return filename

def input_string(filename):
    string = " "
    if exist_checking(filename):
        ch = input("Want To OverWrite {}: (y/n)".format(filename))
        if ch is 'y' or ch is 'Y':
            ofile = openfile(filename)
        else:
            print("Enter Another File Name: ")
            filename = enter_filename()
    else:
        ofile = openfile(filename)
    os.system('clear')
    """ Enter Text: """

    while True:
        string += str(input(">> "))
        string+=string + "\n"
        if ":exit" in string:
            exiting(string, ofile)
        # string+=string + '\n'
        # print(string)
        # input_file(filename, string)

def main():
    if len(argv) is not 2:
        filename = enter_filename()
    else:
        sourcefile, filename = argv
    input_string(filename)

main()
