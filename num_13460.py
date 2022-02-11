
def getInput():
    n, m=list(map(int, input().strip().split()))
    dp=[list(input()) for i in range(n)]
    return n, m, dp

def find(dp):
    bx=0
    by=0
    rx=0
    ry=0
    hx=0
    hy=0
    for i, line in enumerate(dp):
        for j, item in enumerate(line):
            if item=='B':
                bx=i
                by=j
                dp[i][j]='.'
            elif item=='R':
                rx=i
                ry=j
                dp[i][j] = '.'
            elif item=='O':
                hx=i
                hy=j
    return bx, by, rx, ry, hx, hy


def move(cmd, rx, ry, bx, by):
    global n, m, dp

    if cmd==1:
        if ry > by:
            #red move first
            for i in range(ry, m-1):
                if dp[rx][i+1]=='#' or (bx==rx and i+1==by):
                    ry=i
                    break
            for i in range(by, m-1):
                if dp[bx][i+1]=='#' or (bx==rx and i+1==ry):
                    by=i
                    break
        else:
            #blue move first
            for i in range(by, m-1):
                if dp[bx][i+1]=='#' or (bx==rx and i+1==ry):
                    by=i
                    break
            for i in range(ry, m-1):
                if dp[rx][i+1]=='#' or (bx==rx and i+1==by):
                    ry=i
                    break


    elif cmd==2:
        if ry < by:
            for i in range(ry, 0, -1):
                if dp[rx][i-1]=='#' or (bx==rx and i-1==by):
                    ry=i
                    break
            for i in range(by, 0, -1):
                if dp[bx][i-1]=='#' or (bx==rx and i-1==ry):
                    by=i
                    break
        else:
            for i in range(by, 0, -1):
                if dp[bx][i-1]=='#' or (bx==rx and i-1==ry):
                    by=i
                    break
            for i in range(ry, 0, -1):
                if dp[rx][i-1]=='#' or (bx==rx and i-1==by):
                    ry=i
                    break
    elif cmd==3:
        if rx > bx:
            for i in range(rx, n-1):
                if dp[i+1][ry]=='#' or (ry==by and bx==i+1):
                    rx=i
                    break
            for i in range(bx, n-1):
                if dp[i+1][by]=='#' or (ry==by and rx==i+1):
                    bx=i
                    break
        else:
            for i in range(bx, n-1):
                if dp[i+1][by]=='#' or (ry==by and rx==i+1):
                    bx=i
                    break
            for i in range(rx, n-1):
                if dp[i+1][ry]=='#' or (ry==by and bx==i+1):
                    rx=i
                    break
    elif cmd==4:
        if rx < bx:
            for i in range(rx, 0, -1):
                if dp[i-1][ry]=='#' or (ry==by and bx==i-1):
                    rx=i
                    break
            for i in range(bx, 0, -1):
                if dp[i-1][by]=='#' or (ry==by and rx==i-1):
                    bx=i
                    break
        else:
            for i in range(bx, 0, -1):
                if dp[i-1][by]=='#' or (ry==by and rx==i-1):
                    bx=i
                    break
            for i in range(rx, 0, -1):
                if dp[i-1][ry]=='#' or (ry==by and bx==i-1):
                    rx=i
                    break

    return cmd, rx, ry, bx, by

# 1right, 2left, 3up, 4down
def sol(n, m, dp):
    bx, by, rx, ry, hx, hy=find(dp)

    for i in range(4):
        a=1

    move(2, rx, ry, bx, by)







if __name__=="__main__":
    n, m, dp=getInput()
    sol(n, m, dp)