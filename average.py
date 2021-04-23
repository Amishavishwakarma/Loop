#11 logon ka weight input le aur fir average weight print kare. Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi? Note: Isme aapko input ka use karna padega. Aap loop ke andar raw input ka use kar ke 11 baar raw_input le sakte ho.

i=1
a=0
s=0
while i<=5:
    n=int(input("enter your weight"))
    s=s+n
    i=i+1
    a=s/5
print("sum",s)
print("average",a)
if a%5==0:
    print("average hai")
else:
    print("nhi hai")