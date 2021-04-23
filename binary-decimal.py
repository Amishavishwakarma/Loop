#Binry to decimal conversion
n=int(input("enter the number"))
b=n
i=1
c=0
while n>=i:
    c=c+1
    n=n//10
s=0
h=b
f=0
while f<c:
    h=b%10
    s=s+2**f*h
    b=b//10
    f+=1
print(s)