
def getInput():
    n, m=list(map(int, input().strip().split()))
    return n, m

def makenew(line):
    out=[]
    for i in line:
        out.append(i)
    return out

def makeline(num):
    out=[]
    for i in range(num):
        out.append(0)
    return out

def sol(n, m):

    if m==1:
        for i in range(n):
            print(i+1)
    else:
        check=makeline(n)
        for i in range(n):
            temp=makenew(check)
            temp[i]=1
            store=[]
            store.append(i)
            bfs(temp, n, store, 1, m)


def bfs(check, n, store, now, limit):
    if now==limit:
        st=""
        for item in store:
            st+=str(item+1)+" "
        print(st)
    else:
        for i in range(n):
            if i > store[-1]:
                temp=makenew(store)
                temp.append(i)
                bfs(check, n, temp, now+1, limit)

if __name__=="__main__":
    n, m=getInput()
    sol(n, m)