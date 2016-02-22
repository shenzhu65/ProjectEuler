def isPrime(num):
    for i in range(0,len(prime)):
        if num%prime[i] == 0:
            return False
        if prime[i]**2 > num:
            return True

prime = [2]
a = 3
while True:
    if isPrime(a):
        prime.append(a)
    if len(prime) == 10001:
        print(prime[10000])
        break
    a=a+2
    
