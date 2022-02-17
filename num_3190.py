

def getInput():
    n=int(input())
    m=[[0]*n for _ in range(n)]

    k=int(input())
    for i in range(k):
        a, b=list(map(int, input().strip().split()))
        m[a-1][b-1]=-1

    l=int(input())
    out=[]
    for i in range(l):
        a, b=list(input().strip().split())
        out.append([int(a), b])

    return m, out

def printLine(m):
    for i in m:
        print(i)
    print()

# L 왼 D 오
def sol(m, cmd):
    count=0
    n=len(cmd)
    mlen=len(m)

    nowx=0
    nowy=0
    fangxiang=0

    timer, d=cmd.pop(0)

    m[0][0]=1
    snack=[[0,0]]
    t=1

    while True:
        if count==timer:
            if d=='D':
                fangxiang+=1
                if fangxiang > 3:
                    fangxiang=0
            elif d=='L':
                fangxiang-=1
                if fangxiang < 0:
                    fangxiang=3
            if cmd:
                timer, d=cmd.pop(0)

        # move ones
        if fangxiang==0:#오른
            nowy+=1
        elif fangxiang==1:#아래
            nowx+=1
        elif fangxiang==2:#왼쪽
            nowy-=1
        elif fangxiang==3:#윗
            nowx-=1

        # count up
        count += 1

        # wall
        if nowx >= mlen or nowx < 0 or nowy >= mlen or nowy < 0:
            break

        # get apple
        if m[nowx][nowy]==-1:
            m[nowx][nowy]=1
            snack.append([nowx, nowy])
        # touch my body
        elif m[nowx][nowy] > 0:
            break
        # no apple just move
        else:
            m[nowx][nowy]=1
            snack.append([nowx, nowy])
            x, y=snack.pop(0)
            m[x][y]=0
        #print(count)
        #printLine(m)
    print(count)

if __name__=="__main__":
    m, cmd=getInput()
    sol(m, cmd)