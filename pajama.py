n=int(input(" "))
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    for s in range(i):
        print(" ",end=" ")
    for s in range(i):
        print(" ",end=" ")   
    for j in range(n-i+1):
        print("*",end=" ")
    print()
