
def printLine(m):
    for i in m:
        print(i)
    print()

def getInput():
    n, m, x, y, k=list(map(int, input().strip().split()))

    dp=[list(map(int, input().strip().split())) for _ in range(n)]

    cmd=list(map(int, input().strip().split()))

    return x, y, dp, cmd

def sol(x, y, dp, cmd):
    down = 0
    dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    b=len(dp)
    a=len(dp[0])

    nowx=x
    nowy=y

    # right, left, up, down
    for item in cmd:
        if item==1:
            # position change
            if nowy + 1 >= a:
                continue
            else:
                nowy+=1

            # move dice
            temp=dice[1][2]
            dice[1][2]=dice[1][1]
            dice[1][1]=dice[1][0]
            dice[1][0]=down
            down=temp

            # check dice and map
            if dp[nowx][nowy]==0:
                dp[nowx][nowy]=down
            else:
                down=dp[nowx][nowy]
                dp[nowx][nowy]=0

            print(dice[1][1])

        elif item==2:
            # position change
            if nowy-1 < 0:
                continue
            else:
                nowy-=1

            #move dice
            temp=dice[1][0]
            dice[1][0]=dice[1][1]
            dice[1][1]=dice[1][2]
            dice[1][2]=down
            down=temp

            # check dice and map
            if dp[nowx][nowy] == 0:
                dp[nowx][nowy] = down
            else:
                down = dp[nowx][nowy]
                dp[nowx][nowy] = 0

            print(dice[1][1])

        elif item==3:
            # position change
            if nowx-1 < 0:
                continue
            else:
                nowx-=1

            # move dice
            temp=dice[0][1]
            dice[0][1]=dice[1][1]
            dice[1][1]=dice[2][1]
            dice[2][1]=down
            down=temp

            # check dice and map
            if dp[nowx][nowy] == 0:
                dp[nowx][nowy] = down
            else:
                down = dp[nowx][nowy]
                dp[nowx][nowy] = 0

            print(dice[1][1])

        elif item==4:
            # position change
            if nowx+1 >= b:
                continue
            else:
                nowx+=1

            #move dice
            temp=dice[2][1]
            dice[2][1]=dice[1][1]
            dice[1][1]=dice[0][1]
            dice[0][1]=down
            down=temp

            # check dice and map
            if dp[nowx][nowy] == 0:
                dp[nowx][nowy] = down
            else:
                down = dp[nowx][nowy]
                dp[nowx][nowy] = 0

            print(dice[1][1])



if __name__=="__main__":
    x, y, dp, cmd=getInput()
    sol(x, y, dp, cmd)
