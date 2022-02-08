import sys
input = sys.stdin.readline

def getInput():
    r, c=list(map(int, input().strip().split()))

    out=[]
    for i in range(r):
        out.append(list(input()))

    return r, c, out

def pr(m):
    for i in m:
        print(i)
    print("-----------")

def sol(r, c, m):
    dp=[[False]*(c+1) for _ in range(r)]

    for i in range(r):
        if m[i][0]=='.':
            dp[i][0]=True

    for i in range(c):
        for j in range(r):
            if dp[j][i]:
                if j-1 >=0 and m[j-1][i+1]=='.' and not dp[j-1][i+1]:
                    dp[j-1][i+1]=True
                elif m[j][i+1]=='.'and not dp[j][i+1]:
                    dp[j][i+1]=True
                elif j+1 < r and m[j+1][i+1]=='.' and not dp[j+1][i+1]:
                    dp[j+1][i+1]=True

    #pr(dp)

    hap=0
    for z in range(r):
        if dp[z][-2]:
            hap+=1
    print(hap)

if __name__=="__main__":
    r, c, m=getInput()
    sol(r, c, m)