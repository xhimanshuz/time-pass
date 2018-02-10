#!/usr/bin/python3
def fact(n, i):
    pass

def ux(u, i):
    pass
    

def main():
    s = int(input("Enter No. of Row: "))
    x = []
    y = []
    y_row = []
    print("Enter X: ")
    for i in range(s):
        x.append(int(input("X>> ")))

    for i in range(s):
        y_row.append(int(input("Y>> ")))
    y.append(y_row)

    print("X Y")
    for i in range(s):
        print("{} {}".format(x[i], y[0][i]))

    for j in range(1, s):
        y_row = []
        for i in range(s-j):
            y_row.append(y[j-1][i+1]-y[j-1][i])
        y.append(y_row)
    for j in range(s):
        print("-------")
        for i in range(s-j):
            print("{}\t| ".format(y[i][j]), end=" ")
        print()
    print(x[0])
    xi = float(input("Enter X: "))
    h = (x[1]-x[0])
    print("h: {}".format(h))
    u = (xi-x[0])/h
    print("h:{} u:{}".format(h, u))
if __name__ == "__main__":
    main()