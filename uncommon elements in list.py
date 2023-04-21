lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst3=[]
for i in lst1 :
    if i not in lst2: 
        lst3.append(i)
for i in lst2:
    if i not in lst1:
        lst3.append(i)
print(lst3)
or we can do same ques by:-
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
print(lst1)
print(lst2)
lst3=[]
lst4=[]
if lst1>lst2:
    lst4=lst1
else:
    lst4=lst2
for i in lst1:
    if i in lst2:
        lst3.append(i)
for j in lst3:
    lst1.remove(j)
    lst2.remove(j)
lst4=lst1+lst2
print(f"The common elements are : {lst3}")
print(f"The uncommon elements are : {lst4}")
