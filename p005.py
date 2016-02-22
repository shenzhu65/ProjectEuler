def gcd(a,b):
    if a > b:
        return gcd(b,a)
    if b%a == 0:
        return a
    return gcd(b%a, a)

ans = 1

for i in range(1,20):
    ans = ans*i//gcd(ans,i)
print(ans)
