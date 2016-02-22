import math

fac=math.factorial(100)
ans=0
while fac>0:
    ans+=fac%10
    fac//=10
print(ans)
