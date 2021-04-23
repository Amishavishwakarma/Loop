#Factorial 
p=1
n=int(input("enter the numbers"))
while n>0:
    p=p*n
    print(n,"*",end=" ")
    n-=1
print("=",p)
