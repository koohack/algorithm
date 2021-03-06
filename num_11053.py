mx=0

def getInput():
    size=int(input())
    line=list(map(int, input().strip().split()))

    return size, line

def makelist(num):
    out=[]
    for i in range(num):
        out.append(0)
    return out

def makenew(line):
    out=[]
    for i in line:
        out.append(i)
    return out

def bfs(check, line, now, pre, count):
    global mx

    if mx < count:
        mx=count

    for i, item in enumerate(line):
        if i > now and check[i]==0:
            if pre < item:
                temp = makenew(check)
                temp[i] = 1
                bfs(temp, line, i, item, count+1)
            else:
                if mx < count:
                    mx=count
    return

def sol(size, line):
    check=makelist(size)

    for i, item in enumerate(line):
        temp=makenew(check)
        temp[i]=1
        bfs(temp, line, i, item, 1)

def sol1(size, line):
    dp=makelist(size)

    for i in range(size):
        for j in range(i):
            if line[i] > line[j] and dp[i] < dp[j]:
                dp[i]=dp[j]
        dp[i]+=1
    print(max(dp))

if __name__=="__main__":
    size, line=getInput()
    sol1(size, line)
