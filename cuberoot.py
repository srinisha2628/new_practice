x= int(input("enter a number\n"))
ans=0
while ans**3 < abs(x):
    ans+=1
if(ans**3!= abs(x)):
    print("it is not a perfect cube")
else:
    if(x<0):
        ans = -ans
    print("cube root of "+ str(x)+" is "+ str(ans))


cube=int(input("enter a number"))
for guess in range(cube+1):
    if(guess**2==cube):
        print("cube root of",cube ,"is",guess)
