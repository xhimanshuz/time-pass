#!/usr/bin/python3
# LINEAR SEARCH SIMPLE PROGRAM

from sys import argv

class LinearSearch:
    def __init__(self, size=None):
        self.size = size
        self.array = []
        self.flag = 0
        self.count = 0
    
    def algo(self):
        for i in range(self.size):
            self.count+=1
            print(self.count)
            if self.n is self.array[i]:
                print("Found at index number {}".format(i))
                self.flag = 1
                break
        if self.flag is 0:
            print("Element not Found")
    
    def inp(self):
        print("Enter {} Elements in an array: ".format(self.size))
        for i in range(self.size):
            self.array.append(i)
        self.n = int(input("Enter Element to Search its Location: "))

def main():
    if (len(argv))>1:
        size = int(argv[1])
    else:
        size = int(input("Enter Size of Array: ") )
    ls = LinearSearch(size)
    ls.inp()
    ls.algo()

if __name__ == '__main__':
    main()
