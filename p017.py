#words of numbers from one to nineteen(leading 0)
wordsBelow20=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
#words of numbers from twenty to ninty by ten(leading 0 and 10)
wordsBelow100=[0,0,6,6,5,5,5,7,6,6]
#words of 'hundred'
wordsHundred = 7

ans = 0
for i in range(1,1000):
    #number above hundred
    numAbove100 = i//100
    #number below hundred
    numBelow100 = i%100
    if numAbove100>0:
        ans += wordsBelow20[numAbove100] + wordsHundred
    #if both of them are greter than 0, it need an "and" to link them
    if numAbove100>0 and numBelow100>0:
        ans += 3
    if numBelow100<20:
        ans += wordsBelow20[numBelow100]
    else:
        ans += wordsBelow100[numBelow100//10] + wordsBelow20[numBelow100%10]
#one thousan counts 11 num
print(ans+11)
    

