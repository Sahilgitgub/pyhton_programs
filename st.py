lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
        print(i)
