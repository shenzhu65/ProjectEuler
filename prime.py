import math

def __isPrime(num, bFg):
    for i in range(2, int(math.sqrt(num))):
        if bFg[i] :
            if num%i == 0:
                return False
    return True

def makePrimesBelowReturnBoolean(TopLine):
    bIsPrime = [True]*TopLine
    for st in range(2, TopLine):
        if bIsPrime[st] and __isPrime(st, bIsPrime):
            dBrush = st*2
            while dBrush < TopLine:
                bIsPrime[dBrush] = False
                dBrush += st
        else:
            bIsPrime[st] = False
    return bIsPrime

def makePrimesBelowReturnArray(TopLine):
    bIsPrime = makePrimesBelowReturnBoolean(TopLine)
    aPrime = []
    for i in range(2,len(bIsPrime)):
        if bIsPrime[i]:
            aPrime.append(i)
    return aPrime


