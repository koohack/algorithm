from collections import deque

def getInput():
    n=int(input())
    dp=[list(map(int, input().strip().split())) for i in range(n)]

    return n, dp

def sol(n, dp):

    dy=[0, -1, 1, 0]
    dx=[-1, 0, 0, 1]

    fishes=[]
    nowx=0
    nowy=0

    ## find fish
    for i in range(n):
        for j in range(n):
            if 0 < dp[i][j] < 7:
                fishes.append([i, j, dp[i][j]])

            if dp[i][j] == 9:
                nowx=i
                nowy=j

    ## if no fish
    length=len(fishes)
    if length==0:
        print(0)
        return

    ## get direction
    q=deque()
    q.append([nowx, nowy])
    prex=nowx
    prey=nowy
    answer=0
    eat=0

    shark=2
    while length:

        ## bfs search
        visited=[[0]*n for i in range(n)]
        visited[prex][prey]=1
        while q:
            i, j=q.popleft()

            for z in range(4):
                x=i+dx[z]
                y=j+dy[z]

                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    if dp[x][y] == 0 or dp[x][y]==shark:
                        if visited[x][y]==0 or visited[x][y] > visited[i][j]+1:
                            visited[x][y] = visited[i][j] + 1
                            q.append([x, y])
                    elif dp[x][y] < shark:
                        if visited[x][y] == 0 or visited[x][y] > visited[i][j] + 1:
                            visited[x][y] = visited[i][j] + 1
                            q.append([x, y])
                    elif dp[x][y] > shark:
                        continue

        mn=9999999999999
        gox=0
        goy=0
        flag=0
        for i in range(n):
            for j in range(n):
                # dp에서 물고기 존재해야 함, size most smaller than shark, distance minimum
                if 1 < visited[i][j] and 0 < dp[i][j] < shark and visited[i][j] < mn:
                    flag=1
                    mn=visited[i][j]
                    gox=i
                    goy=j

        # eat
        if flag:
            eat+=1
            length-=1
        # can not eat
        else:
            break

        # eat==size
        if eat==shark:
            shark+=1
            eat=0

        # distance
        answer+=visited[gox][goy]-1

        # change
        dp[prex][prey]=0
        dp[gox][goy]=9
        prex=gox
        prey=goy

        q.append([gox, goy])

        #print("================")
        #for z in visited:
         #   print(z)
        #print("------")
        #for z in dp:
         #   print(z)
        #print("================")
        #print(answer, shark, eat)

    print(answer)

if __name__=="__main__":
    n, dp=getInput()
    sol(n, dp)