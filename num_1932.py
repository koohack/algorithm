
def getInput():
    num=int(input())
    out=[]
    for i in range(num):
        t=list(map(int, input().strip().split()))
        out.append(t)

    return num, out

def makeline(num):
    out=[]
    for i in range(num):
        t=[]
        for j in range(num):
            t.append(0)
        out.append(t)
    return out

def sol(n, tri):
    check=makeline(n)
    check[0][0]=tri[0][0]

    for i, line in enumerate(tri):
        if i+1 < n:
            length=len(tri[i+1])

            for j, item in enumerate(line):
                if check[i+1][j] < check[i][j]+tri[i+1][j]:
                    check[i+1][j]=check[i][j]+tri[i+1][j]
                if j+1 < length:
                    if check[i+1][j+1] < check[i][j]+tri[i+1][j+1]:
                        check[i+1][j+1]=check[i][j]+tri[i+1][j+1]

    return max(check[-1])


if __name__=="__main__":
    n, tri=getInput()
    print(sol(n, tri))