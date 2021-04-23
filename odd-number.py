#write 1 to 10 odd number product
i=1
s=0
while i<=10:
    if i%2!=0:
        print(i)
        s=s+(i*i)
    i=i+1
print("product"