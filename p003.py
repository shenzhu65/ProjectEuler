def isPrime(num):
    for i in range(0, len(prime)-1):
        if factor%prime[i] == 0:
            return False
    return True

a,i,ans = 600851475143,2,0
prime = [2]
factor = 2
while factor<=a:
    factor = prime[len(prime)-1]
    if a%factor == 0:
        ans,a = factor,a/factor
    else:
        while 1:
            factor = factor+1
            if isPrime(factor):
                prime.append(factor)
                break
print(ans, a)
            
        
    
