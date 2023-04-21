
#define a function to find out a factorial of a number
def fact():
    a=int(input("Enter the number: "))
    fac=1
    for i in range(1,a+1):
        fac=fac*i
    print(fac)
fact()
        
