import copy

def printde(de):
    for i in de:
        print(i)
    print("-------------")

def getInput():
    n, m=list(map(int, input().strip().split()))
    dp=[list(map(int, input().strip().split())) for i in range(n)]

    return n, m, dp

def east(i, j, n, m, dp):
    for z in range(j + 1, m):
        if dp[i][z] == 0:
            dp[i][z] = '#'
        elif dp[i][z] == 6:
            break
def west(i, j, n, m, dp):
    for z in range(j - 1, -1, -1):
        if dp[i][z] == 0:
            dp[i][z] = '#'
        elif dp[i][z] == 6:
            break
def north(i, j, n, m, dp):
    for z in range(i - 1, -1, -1):
        if dp[z][j] == 0:
            dp[z][j] = '#'
        elif dp[z][j] == 6:
            break
def south(i, j, n, m, dp):
    for z in range(i + 1, n):
        if dp[z][j] == 0:
            dp[z][j] = '#'
        elif dp[z][j] == 6:
            break

def draw(i, j, num, d, dp):
    if num==1:
        if d==0:# right
            east(i, j, n, m, dp)
        elif d==1:# west:
            west(i, j, n, m, dp)
        elif d==2:# north
            north(i, j, n, m, dp)
        elif d==3:# south
            south(i, j, n, m, dp)
    if num==2:
        if d==0:
            east(i, j, n, m, dp)
            west(i, j, n, m, dp)
        elif d==1:
            north(i, j, n, m, dp)
            south(i, j, n, m, dp)
    if num==3:
        if d==0:
            east(i, j, n, m, dp)
            north(i, j, n, m, dp)
        elif d==1:
            east(i, j, n, m, dp)
            south(i, j, n, m, dp)
        elif d==2:
            west(i, j, n, m, dp)
            north(i, j, n, m, dp)
        elif d==3:
            west(i, j, n, m, dp)
            south(i, j, n, m, dp)
    if num==4:
        if d==0:
            east(i, j, n, m, dp)
            west(i, j, n, m, dp)
            north(i, j, n, m, dp)
        elif d==1:
            east(i, j, n, m, dp)
            west(i, j, n, m, dp)
            south(i, j, n, m, dp)
        elif d==2:
            north(i, j, n, m, dp)
            south(i, j, n, m, dp)
            east(i, j, n, m, dp)
        elif d==3:
            north(i, j, n, m, dp)
            south(i, j, n, m, dp)
            west(i, j, n, m, dp)
    if num==5:
        north(i, j, n, m, dp)
        south(i, j, n, m, dp)
        west(i, j, n, m, dp)
        east(i, j, n, m, dp)


def dfs(prei, store, main, l):
    global answer, dp, n, m

    if prei < l:
        if store[prei][2]==1:
            for i in range(4):
                a, b, c=store[prei]
                temp=copy.deepcopy(main)
                temp.append([a, b, c, i])
                dfs(prei+1, store, temp, l)

        elif store[prei][2]==2:
            for i in range(2):
                a, b, c=store[prei]
                temp=copy.deepcopy(main)
                temp.append([a, b, c, i])
                dfs(prei+1, store, temp, l)

        elif store[prei][2]==3:
            for i in range(4):
                a, b, c=store[prei]
                temp=copy.deepcopy(main)
                temp.append([a, b, c, i])
                dfs(prei+1, store, temp, l)

        elif store[prei][2]==4:
            for i in range(4):
                a, b, c=store[prei]
                temp=copy.deepcopy(main)
                temp.append([a, b, c, i])
                dfs(prei+1, store, temp, l)

        elif store[prei][2]==5:
            a, b, c = store[prei]
            temp = copy.deepcopy(main)
            temp.append([a, b, c, 0])
            dfs(prei + 1, store, temp, l)
    else:
        #print(main)
        t=copy.deepcopy(dp)
        for i, j, num, d in main:
            draw(i, j, num, d, t)
        #printde(t)
        count=0
        for i in range(n):
            for j in range(m):
                if t[i][j]==0:
                    count+=1
        if count < answer:
            answer=count



def sol(n, m, dp):

    store=[]
    for i in range(n):
        for j in range(m):
            if 0 < dp[i][j] < 6:
                store.append([i,j,dp[i][j]])

    dfs(0, store, [], len(store))

if __name__=="__main__":
    answer=9999999999999999999999999
    n, m, dp=getInput()
    sol(n, m, dp)
    print(answer)