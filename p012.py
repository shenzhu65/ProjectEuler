import prime

listPrime = prime.makePrimesBelow(100000)

print("Prime Calculation Completed!")
i,sum = 1,0
while True:
    sum += i
    i += 1
    s,fac = sum,1
    for loopi in range(2,100000):
        if listPrime[loopi]:
            t=0
            while s%loopi==0:
                s,t = s//loopi,t+1
            fac *= t+1
        if s==1:
            break
    if fac>500:
        print(sum)
        break
                
                
            
