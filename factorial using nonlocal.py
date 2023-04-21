def fact_sum(y):
    factsum=0
    for i in range(1,y+1):
        f=1
        def fact(i):
            nonlocal f,factsum
            for j in range(1,i+1):
                f*=j
            factsum+=f
    fact(i)
    return factsum
n=int(input("Enter te number: "))
print(fact_sum(n))
