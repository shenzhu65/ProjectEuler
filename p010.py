def isPrime(num):
    for i in range(0,len(prime)):
        if num%prime[i] == 0:
            return False
        if prime[i]**2 > num:
            return True

prime = [2]
a,sum = 3,2
for a in range(3,2000000,2):
    if isPrime(a):
        prime.append(a)
        sum+=a
print(sum)
