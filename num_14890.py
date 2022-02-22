
def getInput():
    n, l=list(map(int, input().strip().split()))
    out=[list(map(int, input().strip().split())) for i in range(n)]

    return n, l, out

def sol(n, l, out):
    count=0
    for i in range(n):
        if check(out[i], n, l):
            count+=1

    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(out[j][i])
        if check(temp, n, l):
            count+=1

    print(count)


    return

def check(line, n, l):
    dp=[0]*n

    for i in range(n-1):
        if line[i]==line[i+1]:
            continue
        if abs(line[i]-line[i+1]) > 1:
            return False
        if line[i]>line[i+1]:
            temp=line[i+1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if line[j]!=temp: return False
                    if dp[j]==1: return False
                    dp[j]=1
                else:
                    return False
        else:
            temp=line[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if line[j]!=temp: return False
                    if dp[j]==1: return False
                    dp[j]=1
                else:
                    return False
    return True

if __name__=="__main__":
    n, l, out=getInput()
    answer=0
    sol(n, l, out)