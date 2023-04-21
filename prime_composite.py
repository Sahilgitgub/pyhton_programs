#prime number come forward and composite go backward
def prime(n):
    if(n>1):
        for i in range(1,n):
            if(n%i==0):
                return 1
        return 0
lst=list(map(int,input().split()))
lst.sort()
lst.sort(key=prime)
print(lst)