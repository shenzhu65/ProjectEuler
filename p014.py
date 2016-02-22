maxa,ans=1,1
for i in range(2,1000000):
    t,p=i,1
    while t!=1:
        if t%2==0:
            t,p=t//2,p+1
        else:
            t,p=t*3+1,p+1
    if p>maxa:
        maxa,ans=p,i
print(ans,maxa)
            
