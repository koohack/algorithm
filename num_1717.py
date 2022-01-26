import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def getInput():
    n, m=listnum(map(int, input().strip().split()))

    return n, m

def sol(n, m):

    check=[]
    for i in range(n+1):
        check.append(i)

    for i in range(m):
        cmd, a, b=list(map(int, input().strip().split()))

        if cmd==0:
            union(check, a, b)
        else:
            t1=find(check, a)
            t2=find(check, b)
            if t1==t2:
                print("YES")
            else:
                print("NO")

def find(check, x):

    if check[x]==x:
        return x
    check[x]=find(check, check[x])
    return check[x]

def union(check, a, b):
    a=find(check, a)
    b=find(check, b)

    if a < b:
        check[b]=a
    else:
        check[a]=b

if __name__=="__main__":
    n, m=getInput()
    sol(n, m)
