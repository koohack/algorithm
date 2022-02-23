

def getInput():
    n, m, h=list(map(int, input().strip().split()))
    cmd=[list(map(int, input().strip().split())) for _ in range(m)]

    return n, m, h, cmd

def godown(num, dp, n, h):
    now=0
    while True:
        if now==h: return num
        if num-1 >= 0 and dp[now][num-1]==1:
            num-=1
        elif dp[now][num]==1:
            num+=1
        now+=1

def track(dp, n, h):
    for i in range(n):
        if godown(i, dp, n, h)!=i:
            return 0
    return 1


def dfs(preh, now, limit, dp, n, h):
    global answer
    if now==limit:
        if track(dp, n, h):
            answer=limit
            return 1
    else:
        for i in range(preh, h):
            for j in range(n-1):
                if (j-1 >=0 and dp[i][j-1]==0 and dp[i][j]==0) or (j-1 < 0 and dp[i][j]==0):
                    dp[i][j]=1
                    dfs(i, now+1, limit, dp, n, h)
                    dp[i][j]=0

        return 0

def sol(n, h, cmd):
    global answer

    dp=[[0]*n for i in range(h+1)]

    for a, b in cmd:
        dp[a-1][b-1]=1

    for count in range(0, 4):
        for i in range(h):
            for j in range(n-1):
                if (j-1 >=0 and dp[i][j-1]==0 and dp[i][j]==0) or (j-1 < 0 and dp[i][j]==0):
                    dp[i][j]=1
                    dfs(i, 1, count, dp, n, h)
                    dp[i][j]=0
                    if answer > 0:
                        print(answer)
                        return
    print(-1)


if __name__=="__main__":
    answer=0
    n, m, h, cmd=getInput()
    sol(n, h, cmd)