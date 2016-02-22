arr = [[1]*21]*21

for i in range(1,21):
    for j in range(1,21):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
print(arr[20][20])
