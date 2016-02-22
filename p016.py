a,ans=2**1000,0
while a>9:
    ans += a%10
    a = a//10
ans += a
print(ans)
