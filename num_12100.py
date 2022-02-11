import copy
from collections import deque

def getInput():
    n=int(input())
    out=[list(map(int, input().strip().split())) for i in range(n)]

    return n, out

def move(cmd, store, n):
    if cmd==1:
        for i in range(n):
            v=[False]*n
            for j in range(n-1, 0, -1):
                if store[i][j]==store[i][j-1] and not v[j]:
                    v[j]=True
                    v[j-1]=True
                    store[i][j]+=store[i][j-1]
                    store[i][j-1]=0
            out=[]
            for k in range(n):
                if store[i][k]!=0:
                    out.append(store[i][k])
            out=[0]*(n-len(out))+out
            store.pop(i)
            store.insert(i, out)
        return store

    elif cmd==2:
        for i in range(n):
            v=[False]*n
            for j in range(n-1):
                if store[i][j]==store[i][j+1] and not v[j]:
                    v[j]=True
                    v[j+1]=True
                    store[i][j]+=store[i][j+1]
                    store[i][j+1]=0
            out=[]
            for k in range(n):
                if store[i][k]!=0:
                    out.append(store[i][k])
            out+=[0]*(n-len(out))
            store.pop(i)
            store.insert(i, out)
        return store

    elif cmd==3:
        for i in range(n):
            v=[False]*n
            for j in range(n-1):
                if store[j][i]==store[j+1][i] and not v[j]:
                    v[j]=True
                    v[j+1]=True
                    store[j][i]+=store[j+1][i]
                    store[j+1][i]=0
            out=[]
            for k in range(n):
                if store[k][i]!=0:
                    out.append(store[k][i])

            for k in range(n):
                if out:
                    store[k][i]=out.pop(0)
                else:
                    store[k][i]=0
        return store

    elif cmd==4:
        for i in range(n):
            v=[False]*n
            for j in range(n-1, 0, -1):
                if store[j][i]==store[j-1][i] and not v[j]:
                    v[j]=True
                    v[j-1]=True
                    store[j][i]+=store[j-1][i]
                    store[j-1][i]=0

            out = []
            for k in range(n):
                if store[k][i] != 0:
                    out.append(store[k][i])

            for k in range(n-1, 0, -1):
                if out:
                    store[k][i] = out.pop(0)
                else:
                    store[k][i] = 0
        return store

def getMax(store):
    mx=0
    for line in store:
        temp=max(line)
        mx=max(mx, temp)
    return mx

def sol(n, store):
    q=deque()

    count=1
    for i in range(4):
        temp=copy.deepcopy(store)
        out=move(i+1, temp, n)
        q.append([out, 1])

    mx=0
    while q:
        now, count=q.popleft()
        if count < 5:
            for i in range(4):
                temp=copy.deepcopy(now)
                out=move(i+1, temp, n)
                if count+1==5:
                    mx=max(mx, getMax(out))
                q.append((out, count+1))

    print(mx)

if __name__=="__main__":
    n, store=getInput()
    sol(n, store)