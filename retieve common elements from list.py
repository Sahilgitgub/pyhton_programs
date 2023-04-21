lst1=list(map(int,input("Input for list 1: ").split()))
lst2=list(map(int,input("Input for list 2: ").split()))
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)
