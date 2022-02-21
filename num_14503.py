
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

    while True:

        print(x, y, count)
        printdp(dp)

        check=0
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        for i in range(4):
            tempx=x
            tempy=y
            tempx+=dx[i]
            tempy+=dy[i]

            if not (0 <= tempx < n and 0 <= tempy < m):
                check+=1
            elif dp[tempx][tempy]==1 or dp[tempx][tempy]==-1:
                check+=1

        if check==4:
            if fangxiang==0:
                if x+1 > n:
                    print("0-1")
                    break
                elif dp[x+1][y]==-1:
                    x+=1
                elif dp[x+1][y]==1:
                    print("0-2")
                    break

            elif fangxiang==1:
                if y-1 < 0:
                    print("1-1")
                    break
                elif dp[x][y-1]==-1:
                    y-=1
                elif dp[x][y-1]==1:
                    print("1-2")
                    break

            elif fangxiang==2:
                if x-1 < 0:
                    print("2-1")
                    break
                elif dp[x-1][y]==-1:
                    x-=1
                elif dp[x-1][y]==1:
                    print("2-2")
                    break

            elif fangxiang==3:
                if y+1 > m:
                    print("3-1")
                    break
                elif dp[x][y+1]==-1:
                    y+=1
                elif dp[x][y+1]==1:
                    print("3-2")
                    break


        fangxiang+=1
        fangxiang=fangxiang%4

        if fangxiang==0:
            if y-1 >= 0:
                if dp[x][y-1]==0:
                    dp[x][y-1]=-1
                    y-=1
                    count+=1

        elif fangxiang==1:
            if x+1 < n:
                if dp[x+1][y]==0:
                    dp[x+1][y]=-1
                    x+=1
                    count+=1

        elif fangxiang==2:
            if y+1 < m:
                if dp[x][y+1]==0:
                    dp[x][y+1]=-1
                    y+=1
                    count+=1

        elif fangxiang==3:
            if x-1 >= 0:
                if dp[x-1][y]==0:
                    dp[x-1][y]=-1
                    x-=1
                    count+=1


    print(count)




if __name__=="__main__":
    dp, x, y, fangxiang=getInput()
    sol(dp, x, y, fangxiang)