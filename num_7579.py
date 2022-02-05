import copy, sys
input = sys.stdin.readline

def getInput():
    n, m=map(int, input().strip().split())
    mem=[0]+list(map(int, input().strip().split()))
    re=[0]+list(map(int, input().strip().split()))

    return n, m, mem, re

def sol(n, m, mem, re):
    hap=sum(re)
    dp=[[0 for _ in range(hap+1)] for _ in range(n+1)]


    for i in range(1, n+1):
        byte=mem[i]
        cost=re[i]

        for j in range(1, hap+1):
            if j < cost:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(byte+dp[i-1][j-cost], dp[i-1][j])


    for i, item in enumerate(dp[-1]):
        if item >= m:
            print(i)
            break

if __name__=="__main__":
    n, m, mem, re=getInput()
    sol(n, m, mem, re)
