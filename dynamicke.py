b, a = [int(x) for x in input().split()]
memo = [[-1 for i in range(b+1)] for x in range(a+1)]


memo[0] = list(map(lambda x: 0, memo[0]))
for x in range(a+1):
    memo[x][0] = 1


for row in range(1,a+1):
    for col in range(1,b+1):
        memo[row][col] = memo[row][col-1]/2 + memo[row-1][col]/2
        
print(memo[a][b])




