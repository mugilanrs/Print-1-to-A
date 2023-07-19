# PRINT 1 to A

def printNums(A):
    if A == 1:
        print(A)
        return
    printNums(A - 1)
    print(A)

A = int(input("Enter an integer A: "))
printNums(A)
