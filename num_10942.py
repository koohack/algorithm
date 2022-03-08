import sys
input = sys.stdin.readline



def getInput():
    n=int(input())
    line=list(map(int, input().strip().split()))

    m=int(input())

    return line, m

def sol(line, m):
    n=len(line)
    dp=[[0]*n for i in range(n)]


    for i in range(n):
        dp[i][i]=1
    for i in range(n-1):
        if line[i]==line[i+1]:
            dp[i][i+1]=1

    for l in range(2, n):
        for i in range(n-l):
            if line[i]==line[i+l] and dp[i+1][i+l-1]==1:
                dp[i][i+l]=1

    for _ in range(m):
        i, j=map(int, input().strip().split())
        print(dp[i-1][j-1])

if __name__=="__main__":
    line, m=getInput()
    sol(line, m)