from sys import argv

def ia():
    print("ai()")
    #pass
def ao():
     print("ao()")

def del_a():
    print("del_a()")
def cc():
    print("Exit")


def switch_cs():
    c = 0
    choice = {
    1: ia(),
    2: ao(),
    3: del_a(),
    4: cc() }
    while c != 1:
        cn = int(raw_input("1. Input Array \n2. Output Array \n3. Delelete Array \n4.Exit \nEnter Your Choice: "))
        print(cn)
        choice[cn]

def main():
    a = 1
    switch_cs()

main()
