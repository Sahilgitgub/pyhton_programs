print("palindrome number")
n=int(input(" "))
x=n
rev=0
while(n>0):
    r=n%10
    rev=r+rev*10
    n=n//10
if(rev==x):
    print("number is palindrome")
else:
    print("not a palindrome number")
