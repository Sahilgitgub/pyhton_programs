def issorted(ls):
    t=ls.copy()
    ls.sort()
    if(t==ls):
        return 0;
    elif(t=[::-1]):
        return 1;
    else:
        return -1;
lst=list(map(int,input().split()))
out=issorted(lst)
print(out)
    
