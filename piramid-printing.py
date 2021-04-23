#write a program to print piramid

k=1
i=1 
while i<=2:
    b=1 
    while b<=2-i:
        print("",end=" ")
        b=b+1
    j=1
    while i<=k: 
        print("*",end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1