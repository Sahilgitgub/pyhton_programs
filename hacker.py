lst=eval(input())
r,c=map(int,input().split('x'))
out=[]
count=0
if(r*c==len(lst)):
    for i in range(r):
        t=[]
        for j in range(c):
            t.append(lst[count])
            count+=1
        out.append(t)
    for u in out:
        print(*u)
else:
    print(None)