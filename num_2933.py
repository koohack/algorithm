
from collections import deque

def getInput():
    r, c=list(map(int, input().strip().split()))
    dp=[list(input()) for i in range(r)]
    n=int(input())
    throw=list(map(int, input().strip().split()))
    return r,c,dp,throw

def find(dp, r, c):
    v=[[0]*c for i in range(r)]

    q=deque()
    for i in range(c):
        if dp[r-1][i]=='x':
            v[r-1][i]=1
            q.append([r-1, i])

    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    while q:
        x, y=q.pop()
        for i in range(4):
            nowx=x+dx[i]
            nowy=y+dy[i]
            if 0<=nowx<r and 0<=nowy<c and not v[nowx][nowy] and dp[nowx][nowy]=='x':
                v[nowx][nowy]=1
                q.append([nowx,nowy])
    return v

def godown(dp, x, y, r, c):
    index=r-1
    for i in range(x, r-1):
        if dp[i+1][y]=='x':
            index=i
            break
    dp[x][y]='.'
    dp[index][y]='x'

def sol(r, c, dp, throw):
    d=1

    for item in throw:
        if d==1:
            d=0
            index=0
            flag=0
            for i in range(c):
                if dp[r-item][i]=='x':
                    dp[r-item][i]='.'
                    index=i
                    flag=1
                    break
        else:
            d=1
            index=0
            flag=0
            for i in range(c-1, -1, -1):
                if dp[r-item][i]=='x':
                    dp[r-item][i]='.'
                    index=i
                    flag=1
                    break

        # 블록을 제거했다면
        if flag:
            # 땅에 연결되어 있는 것들
            check=find(dp, r, c)

            # 떨어져있는 블록들 찾기
            line=deque()
            for i in range(r-1, -1, -1):
                for j in range(c):
                    if check[i][j]==0 and dp[i][j]=='x':
                        line.append([i, j])

            # 떨어질 블록이 없을 때
            if not line:
                continue

            # 블록 칠하기
            temp=0

            while not temp:

                store = deque()
                count=len(line)

                for i in range(count):
                    x, y=line[i]
                    if x+1 < r:
                        if dp[x+1][y]=='.':
                            dp[x][y]='.'
                            dp[x+1][y]='x'
                            store.append([x+1, y])
                        elif dp[x+1][y]=='x':
                            #
                            for i in range(len(store)):
                                item=store.pop()
                                dp[item[0]][item[1]]='.'
                                dp[item[0]-1][item[1]]='x'
                            temp=1
                            break
                    else:
                        #
                        for i in range(len(store)):
                            item = store.pop()
                            dp[item[0]][item[1]] = '.'
                            dp[item[0] - 1][item[1]] = 'x'
                        temp=1
                        break

                line=store




if __name__=="__main__":
    r,c,dp,throw=getInput()
    sol(r,c,dp,throw)
    #
    for i in dp:
        print("".join(i))