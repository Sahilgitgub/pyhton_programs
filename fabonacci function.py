#define a function to print a fabonnaci series.
def fabo():
    a=int(input("Enter the number: "))
    n1=0
    n2=1
    print(n1,n2,end=" ")
    while(a>0):
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        a=a-1
fabo()        

