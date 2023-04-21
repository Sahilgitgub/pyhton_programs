def valid_matrix(arr):
    ln=len(arr[0])
    for r in arr:
        if(len(r)!=ln):
            return False
    return True
mat=[[3,5,6],[2,5,0]]
if(valid_matrix(mat)):
    for r in mat:
        print(*r,sep=" ")
else:
    print("invalid matrix")
