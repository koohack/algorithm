import sys
input = sys.stdin.readline
def getInput():
    a, b=list(map(int, input().strip().split()))
    out=[list(map(int, input().strip().split())) for _ in range(a)]

    return a, b, out

def dfs(ditu, x, y, check, now, limit, hap):
    global answer, a, b, out
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    if now==limit:
        if answer < hap:
            answer=hap
    else:
        for i in range(4):
            nowx=x+dx[i]
            nowy=y+dy[i]

            if 0 <= nowx < a and 0 <= nowy < b and check[nowx][nowy]==0:
                check[nowx][nowy]=1
                dfs(ditu, nowx, nowy, check, now+1, limit, hap+ditu[nowx][nowy])
                check[nowx][nowy]=0

def fuck(dp, i, j):
    global answer, a, b

    if j+1 < b and j-1 >= 0 and i+1 < a:
        answer=max(answer, dp[i][j]+dp[i][j+1]+dp[i][j-1]+dp[i+1][j])
    if j+1 < b and j-1 >= 0 and i-1 >= 0:
        answer = max(answer, dp[i][j] + dp[i][j + 1] + dp[i][j - 1] + dp[i - 1][j])
    if i+1 < a and i-1 >= 0 and j+1 < b:
        answer = max(answer, dp[i][j]+dp[i+1][j]+dp[i-1][j]+dp[i][j+1])
    if i+1 < a and i-1 >= 0 and j-1 >= 0:
        answer = max(answer, dp[i][j] + dp[i + 1][j] + dp[i - 1][j] + dp[i][j - 1])

def sol(a, b, out):
    global answer

    check=[[0]*b for _ in range(a)]

    for i in range(a):
        for j in range(b):
            fuck(out, i, j)
            check[i][j] = 1
            dfs(out, i, j, check, 1, 4, out[i][j])
            check[i][j]=0

    print(answer)

if __name__=="__main__":
    a, b, out=getInput()
    answer=0
    sol(a, b, out)