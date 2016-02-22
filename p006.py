sum1,sum2 = (1+100)*100//2,0

sum1 = sum1**2

for i in range(1,101):
    sum2 = sum2+i**2

print(sum1,sum2,sum1-sum2)


