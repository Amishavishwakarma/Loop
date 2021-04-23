# print factor of input by user 
i=1
f=0
n=int(input("enter any number "))
while i<=n:
    if n%i==0:
        print(i) 
        f=f+1
    i=i+1
if f==2:
    print("prime number")
else:
    print("no prime number")
