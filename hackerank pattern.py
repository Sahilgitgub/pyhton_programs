
n=int(input("Enter the number: "))
m=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==1  or
           j==1 or j==m):
                print(n,end=" ")
        else:
            print(n-1,end=' ')
    for j in range(1,m+1):
        if(j==1 or j==m):
                print(n-2,end=" ")
    print()
