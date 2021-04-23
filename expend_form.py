user=input("enter the number")
j=len(user)-1
for i in range(0,len(user)):
    a=int(user[i])*10**j
    print(str(a),end="")
    if i < len(user)-1:
        print("+",end="")
    j=j-1
print("\n")