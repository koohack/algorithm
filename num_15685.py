def getInput():
    n=int(input())
    cmd=[list(map(int, input().strip().split())) for _ in range(n)]

    return n, cmd

def sol(n, cmd):
    m=[[0]*101 for _ in range(101)]
    dy=[0, -1, 0, 1]
    dx=[1, 0, -1, 0]

    for z in range(n):
        x, y, d, g=cmd[z]
        m[x][y]=1

        cur=[d]
        for _ in range(g):
            temp=[]
            for i in range(len(cur)):
                temp.append( (cur[-i-1]+1) % 4 )
            cur.extend(temp)

        for item in cur:
            nx=x+dx[item]
            ny=y+dy[item]

            m[nx][ny]=1
            x, y = nx, ny

    # check score
    count=0
    for i in range(100):
        for j in range(100):
            if m[i][j] and m[i+1][j] and m[i][j+1] and m[i+1][j+1]:
                count+=1


    print(count)



if __name__=="__main__":
    n, cmd=getInput()
    sol(n, cmd)
