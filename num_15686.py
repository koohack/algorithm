

def getInput():
    n, m=list(map(int, input().strip().split()))
    dp=[list(map(int, input().strip().split())) for i in range(n)]

    return n, m, dp

def dfs(prei, check, now, limit, l, home, store):
    global answer
    # get store
    if now <= limit:

        t=[]
        for i, flag in enumerate(check):
            if flag:
                t.append(store[i])
        # get distance
        distance=[9999999999]*len(home)
        for i, item in enumerate(home):
            for x, y in t:
                hap=abs(x-item[0])+abs(y-item[1])
                if hap < distance[i]:
                    distance[i]=hap
        # answer
        total=sum(distance)
        answer=min(answer, total)
        #print("--------")
        #print(total)
        #print(t)
        #print(check)
        #print(distance)

        for i in range(prei+1, l):
            check[i]=1
            dfs(i, check, now+1, limit, l, home, store)
            check[i]=0




def sol(n, m, dp):
    # 1. 치킨집 list
    # 2. 치킨집 check하면서 dfs
    # 3. 뺸 곳 도달했을 때 check
    store=[]
    home=[]
    for i in range(n):
        for j in range(n):
            if dp[i][j]==1:
                home.append([i,j])
            if dp[i][j]==2:
                store.append([i,j])
    check=[0]*len(store)


    for i in range(len(check)):
        check[i]=1
        dfs(i, check, 1, m, len(store), home, store)
        check[i]=0


if __name__=="__main__":
    answer=99999999999
    n, m, dp=getInput()
    sol(n, m, dp)
    print(answer)