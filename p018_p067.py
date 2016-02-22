#For Problem 18
#file = open('p18.txt','r')
#For Problem 67
file = open('p067_triangle.txt','r')

n,fin=0,file.readline()
arr = []
while fin:
    arr.append([int(t) for t in fin.split(' ')])
    fin = file.readline()
    n+=1

f = [[0 for i in range(n)] for j in range(n)]
f[0][0] = arr[0][0]
maxAns = 0
for i in range(1,n):
    f[i][0]=f[i-1][0]+arr[i][0]
    f[i][i]=f[i-1][i-1]+arr[i][i]
    for j in range(1,i):
        f[i][j] = max(f[i-1][j],f[i-1][j-1])+arr[i][j]
        if f[i][j]>maxAns:
            maxAns=f[i][j]
print(maxAns)
