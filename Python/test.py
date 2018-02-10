#!/usr/bin/python3
#Text File editor
from sys import argv
class Editor():
    def input_string():
        pass

    def __init__(self, filename):
        print("===>__init__")
        self.filename = filename
        print("File: {}".format(self.filename))
        self.ofile = open('self.filename','r+')
        print(self.ofile.read())
        self.line = 1

    def input_file(self, string):
        print("===>input_file")
        print(self.ofile.read())
        ofile.write("Test")

    def input_string(self):
        print("===>input_string")
        while True:
            self.string = str(input(">> "))
            print(self.string)
            self.input_file(self.string)

    def __del__(self):
        print("===>__del__")
        ch = str(input("Do you really want to Exit? (y/n)"))
        if ch is 'y' or ch is 'Y':
            self.ofile.close()
            print("Exit..!")
        else:
            input_string()

def main():
    if len(argv) < 2:
        filename = input("Enter File Name: ")
    else:
        sourcefile, filename = argv
    editor = Editor(filename)
    editor.input_string()

if __name__ == "__main__":
    main()
