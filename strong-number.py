# strong number
sum=0
num=int(input("enter the number"))
t=num
while(num):
    i=1
    f=1
    r=num%10
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if sum==t:
    print("it is a strong number")
else:
    print("it is not a strong number ")