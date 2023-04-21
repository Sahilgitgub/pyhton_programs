n=int(input())
for i in range(1,n+1):
    s=int(input())
    for j in range(1,s+1):
        c=list(map(int(input())))
        z=max(c)
        w=min(c)
print("Min=",w)
print("max=",z)