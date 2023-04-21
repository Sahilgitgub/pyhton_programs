def issorted(ls):
    t=sorted(ls)
    if(t==ls):
        return 0;
    elif(t==lst[::-1]):
        return 1;
    else:
        return -1;
lst=list(map(int,input("Enter the number: ").split()))
out=issorted(lst)
print(out)
