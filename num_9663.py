

def getInput():
    return int(input())

def makelist(num):
    out=[]
    for i in range(num):
        t=[]
        for j in range(num):
            t.append(0)
        out.append(t)
    return out

def makenew(line):
    out=[]
    for li in line:
        t=[]
        for item in li:
            t.append(item)
        out.append(t)
    return out

def sol(n):
    check=makelist(n)

    for i in range(n):
        for j in range(n):
            temp=makenew(check)
            temp[i][j]=1
            bfs(check, i, j, 1, n)

    print(count)


def draw(check, i, j):

    n=len(check)

    for x in range(n):
        check[x][j]=1
    for y in range(n):
        check[i][y]=1

    goi=i
    goj=j
    while True:
        if goi-1 >= 0 and goj-1 >= 0:
            check[goi-1][goj-1]=1
            goi-=1
            goj-=1
        else:
            break
    goi=i
    goj=j
    while True:
        if goi-1 >= 0 and goj+1 < n:
            check[goi-1][goj+1]=1
            goi-=1
            goj+=1
        else:
            break

    goi = i
    goj = j
    while True:
        if goi + 1 < n and goj + 1 < n:
            check[goi + 1][goj + 1] = 1
            goi += 1
            goj += 1
        else:
            break

    goi = i
    goj = j
    while True:
        if goi + 1 < n and goj - 1 >= 0:
            check[goi + 1][goj - 1] = 1
            goi += 1
            goj -= 1
        else:
            break

    return check

def bfs(check, prei, prej, now, limit):
    global count

    if now==limit:
        count+=1
    else:
        for i, line in enumerate(check):
            for j, item in enumerate(line):
                if i>=prei and j>=prej and check[i][j]==0:
                    temp=makenew(check)
                    temp[i][j]=1
                    temp=draw(temp, i, j)
                    bfs(temp, i, j, now+1, limit)



def makelist1(num):
    out=[]
    for i in range(num):
        out.append(0)
    return out

def sol1(n):
    check=makelist1(n)




def bfs1():

    return

if __name__=="__main__":
    n=getInput()
    count=0
    #sol(n)