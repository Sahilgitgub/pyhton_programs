n=int(input("Enter the number: "))
for i in range(1,n+1,1):
    for j in range(n-i):
        print("*",end=" ")
    for s in range(i-1):
        print(" ",end=" ")
    for s in range(i-1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
