def valid_matrix(arr):
    ln = len(arr[0])
    for r in arr:
        if(len(r)!= ln):
            return False
    return True
n=int(input("Enter the number: "))
for i in range(1,n+1):
    mat1 = int(input('Enterthe matrix 1: '))
for i in range(1,n+1):
    mat2 = int(input('Enterthe matrix 2: '))
for i in range(1,n+1):
    mat3 = int(input('Enterthe matrix 3: '))
lst=[mat1,mat2,mat3]
if(valid_matrix(lst)):
    for r in lst:
        print(*r,sep=" ")
else:
    print("invalid matrix")
