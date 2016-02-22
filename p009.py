for a in range(1,334):
    for b in range(a+1,(1000-a)//2+1):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print(a,b,c,a*b*c)
