import copy, sys
input = sys.stdin.readline

def getInput():
    n, m=map(int, input().strip().split())
    mem=list(map(int, input().strip().split()))
    re=list(map(int, input().strip().split()))

    return n, m, mem, re

def sol(n, m, mem, re):
    hap=sum(re)+1
    dp=[[0 for _ in range(hap)] for _ in range(n)]

    for i in range(hap):
        if re[0] <= i:
            dp[0][i]=mem[0]

    for i in range(n):
        if i==0:
            continue
        for j in range(hap):
            if re[i]+j < hap:
                if dp[i-1][re[i]+j] < dp[i-1][j]+mem[i]:
                    dp[i][re[i]+j]=dp[i-1][j]+mem[i]
                else:
                    dp[i][re[i]+j]=dp[i-1][re[i]+j]

            elif dp[i][j]!=0:
                dp[i][j]=dp[i-1][j]
            elif dp[]

    for i, item in enumerate(dp[-1]):
        if item >= m:
            print(i)
            break

if __name__=="__main__":
    n, m, mem, re=getInput()
    sol(n, m, mem, re)
