n=int(input("Enter the number: "))
for i in range(2,n+1):
    if(n%i==0):
        break;
    print("number is not prime")
    break;
else:
    print("a prime number")
