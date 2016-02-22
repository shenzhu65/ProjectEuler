def isPalindromic(num):
    nbr = []
    while num>0:
        nbr.append(num%10)
        num=num//10
    for i in range(0,(len(nbr)//2)):
        if nbr[i] != nbr[len(nbr)-i-1]:
            return False
    return True

ans = 10000
for a1 in range(100,999):
    for a2 in range(100,999):
        t = a1*a2
        if isPalindromic(t) and t>ans:
            ans = t
print(ans)
