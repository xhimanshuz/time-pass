#!/usr/bin/python3
from sys import argv

class BinarySearch:
    def __init__(self, size, n):
        self.size = 1000
        self.arr = []
        self.pos = -1
        self.count = 0
        self.n = n
    def out(self):
        print(self.arr)
    
    def algo(self):
        start = 0
        end = self.size-1
        while (start<=end):
            mid = int((start+end)/2)
            self.count+=1
            print("{}".format(self.count))
            if self.arr[mid]==self.n:
                self.pos = mid
                print("{} found on {}".format(self.n, self.pos))
                break
            if self.n<self.arr[mid]:
                end = mid - 1
            else:
                start = mid + 1                
        if self.pos is -1:
            print("Not Found..!")
    
    def inp(self):
        #self.n = int(input("Enter N to Search its position: "))
        for i in range(self.size):
            self.arr.append(i)
    
def main():
    if(len(argv)>1):
        sourcefile, size, n = argv
        bs = BinarySearch(int(size), int(n))
    bs.inp()
    bs.algo()
    bs.out()
    
if __name__ == '__main__':
    main()