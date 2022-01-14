
def getInput():
    n, m=list(map(int, input().strip().split()))
    return n, m

def makenew(line):
    out=[]
    for i in line:
        out.append(i)
    return out

def dfs(store, pre, now, limit, n):
    if now==limit:
        st=""
        for i in store:
            st+=str(i+1)+" "
        print(st)
    else:
        for i in range(pre, n):
            temp=makenew(store)
            temp.append(i)
            dfs(temp, i, now+1, limit, n)

def sol(n, m):
    store=[]
    for i in range(n):
        temp=makenew(store)
        temp.append(i)
        dfs(temp, i, 1, m, n)

if __name__=="__main__":
    n, m=getInput()
    sol(n, m)