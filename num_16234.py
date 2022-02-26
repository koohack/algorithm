import sys
sys.setrecursionlimit(2500)

def getInput():
    n, l, r=list(map(int, input().strip().split()))
    out=[list(map(int, input().strip().split())) for i in range(n)]

    return n, l, r, out

def dfs(mex, mey, dp, out, l, r, n, count):
    global store
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        x=mex+dx[i]
        y=mey+dy[i]

        if 0 <= x < n and 0 <= y < n and dp[x][y]==0 and l <= abs(out[mex][mey]-out[x][y]) <= r:
            dp[x][y]=count
            store[count][0]+=out[x][y]
            store[count][1]+=1
            dfs(x, y, dp, out, l, r, n, count)

def sol(n, l, r, out):
    global store

    count=0
    while True:
        store = [[0, 0] for i in range(2501)]
        dp, flag=make(n, l, r, out)
        if not flag:
            #print("stop")
            break

        count+=1

        for i in range(n):
            for j in range(n):
                total=store[dp[i][j]][0]
                num=store[dp[i][j]][1]
                out[i][j]=int(total/num)

    return count

def make(n, l, r, out):
    global store

    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]

    dp=[[0]*n for i in range(n)]

    count=0
    flag=0
    for i in range(n):
        for j in range(n):
            count+=1
            if dp[i][j]==0:
                dp[i][j]=count
                store[count][0]+=out[i][j]
                store[count][1]+=1
                for z in range(4):
                    x=i+dx[z]
                    y=j+dy[z]
                    if 0 <= x < n and 0 <= y < n and dp[x][y]==0 and l <= abs(out[i][j]-out[x][y]) <= r:
                        flag=1
                        dp[x][y]=count
                        store[count][0]+=out[x][y]
                        store[count][1] += 1
                        dfs(x, y, dp, out, l, r, n, count)

    return dp, flag

if __name__=="__main__":
    store=[[0, 0] for i in range(2500)]
    n, l, r, out=getInput()
    answer=sol(n, l, r, out)
    print(answer)