from sys import argv

def linear_search(n):
        array = [1,2,3,4,5,6,7,8,9,0]
        flag = 0
        for i in range(len(array)):
            if n == array[i]:
                flag = 1
                print("%d Found at %d" %(n, i))
        if flag == 0:
            print("Not Found")
def main():
    if(len(argv)==2):
        sourcefile, n = argv
        n = int(n)
        linear_search(n)
    else:
        n = int(raw_input("Enter Number to Find Index No.: \n>> "))
        linear_search(n)
    pass

main()
