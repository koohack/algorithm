
def printdp(dp):
    for i in dp:
        print(i)
    print("-----------")

def getInput():
    n, m=list(map(int, input().strip().split()))
    x, y, fangxiang=list(map(int, input().strip().split()))
    dp=[list(map(int, input().strip().split())) for i in range(n)]

    return dp, x, y, fangxiang

# north, east, north, west
def sol(dp, x, y, fangxiang):
    count=0

    n=len(dp)
    m=len(dp[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dp[x][y]=2
    count+=1

    while True:

        # 4방향에 갈 수 있는 자리 있는지 확인
        empty=0
        for i in range(4):
            tempx=x+dx[(fangxiang+3)%4]
            tempy=y+dy[(fangxiang+3)%4]
            fangxiang = (fangxiang + 3) % 4
            #갈 수 있음
            if 0 < tempx < n and 0 < tempy < m and dp[tempx][tempy]==0:
                empty=1
                x=tempx
                y=tempy
                dp[x][y]=2
                count+=1
                break


        # 갈 곳이 없음
        if not empty:
            if dp[x-dx[fangxiang]][y-dy[fangxiang]]==1:
                print(count)
                break
            else:
                x-=dx[fangxiang]
                y-=dy[fangxiang]


if __name__=="__main__":
    dp, x, y, fangxiang=getInput()
    sol(dp, x, y, fangxiang)