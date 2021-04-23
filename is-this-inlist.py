# Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
# ( Iterate over list using while loop ).

a=[]
i=0
while i<5:
    n=input("enter the number")
    a.append(n)
    i=i+1
print(a)
n2=input("enter the number")
if n2 in a:
    print("yes it is in the list")
else:
    print("it is not in the list")