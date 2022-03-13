

def getInput():
    r,c,t=list(map(int, input().strip().split()))
    dp=[list(map(int, input().strip().split())) for i in range(r)]

    return r,c,t,dp

def sol(r, c, t, dp):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ## inital
    x1, y1, x2, y2=-1, -1, -1, -1
    for i in range(r):
        for j in range(c):
            if dp[i][j]==-1:
                if x1==-1 and y1==-1:
                    x1, y1=i, j
                else:
                    x2, y2=i, j

    for _ in t:
        check=[[0]*c for i in range(r)]
        check[x1][y1]=-1
        check[x2][y2]=-1

        for i in range(r):
            for j in range(c):
                count=0
                temp=dp[i][j]//5

                ## spread
                for z in range(4):
                    x=i+dx[z]
                    y=j+dy[z]
                    if 0<=x<r and 0<=y<c and dp[x][y] > 0:
                        check[x][y]+=temp
                        count+=1

                ## after spread
                check[i][j]-=temp*count
                


if __name__=="__main__":
    r,c,t,dp=getInput()