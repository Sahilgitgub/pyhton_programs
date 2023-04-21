import random
num = random.randint(1,100)
attempts = 5
while attempts:
    user_num=int(input("Enter the number: "))
    attempts-=1
    print(f' attempts left {attempts}')
    if(user_num == num):
        print("you won")
        break;
    elif(user_num < num):
        print("to small with score",attempts)
    else:
        print("to large with score",attempts)
else:
    print("you fail to guess, num is:  ",num)
