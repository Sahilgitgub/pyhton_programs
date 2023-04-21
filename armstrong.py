print("armstrong number")
num=int(input("Enter the number: "))
sum=0
x=num
while(num>0):
    d=num%10
    num=num//10
    sum=sum+(d*d*d)
if(sum==x):
    print("Number is armstrog")
else:
    print("Not a armstrong number")
