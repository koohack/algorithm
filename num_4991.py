from collections import deque

def bfs(fromx, fromy, w, h, dp):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    check=[[0]*w for i in range(h)]

    q=deque()
    q.append([fromx, fromy])

    while q:
        i, j=q.popleft()
        for z in range(4):
            x=i+dx[z]
            y=j+dy[z]
            if 0<=x<h and 0<=y<w and dp[x][y]!='x' and check[x][y]==0:
                check[x][y]=check[i][j]+1
                q.append([x,y])

    return check

def search(now, nowi, dirty, store, dp, w, h):
    check=bfs(now[0], now[1], w, h, dp)
    for i, po in enumerate(dirty):
        if i==nowi:
            store[nowi].append(-1)
        else:
            store[nowi].append(check[po[0]][po[1]])

def dfs(check, store, length, hap, now, prei):
    global answer
    if now==length-1:
        #print(check)
        if hap < answer:
            answer=hap
    else:
        for i in range(1, length):
            if check[i]==0:
                check[i]=1
                dfs(check, store, length, hap+store[prei][i], now+1, i)
                check[i]=0


def sol():
    global answer
    while True:
        w, h = list(map(int, input().strip().split()))
        dp = [list(input()) for i in range(h)]

        if w ==0 and h==0:
            break

        nowx=0
        nowy=0
        dirty=[]
        for i in range(h):
            for j in range(w):
                if dp[i][j]=='o':
                    nowx=i
                    nowy=j
                elif dp[i][j]=='*':
                    dirty.append([i,j])

        dirty.insert(0, [nowx, nowy])
        length=len(dirty)
        store=[[] for i in range(length)]
        for i in range(length):
            search(dirty[i], i, dirty, store, dp, w, h)
            #print(store)

        check=[0]*length
        # 노드 간 거리 모두 합했을 때 최소 찾기
        for i in range(1, length):
            check[i]=1
            dfs(check, store, length, store[0][i], 1, i)
            check[i]=0

        flag=0
        for line in store:
            for item in line:
                if item==0:
                    flag=1
                    break
        if flag:
            print(-1)
            answer = 9999999999999
            continue

        print(answer)
        answer=9999999999999

if __name__=="__main__":
    answer=9999999999999
    sol()