def getInput():
    n, m=list(map(int, input().strip().split()))

    out=[]
    for i in range(n):
        t=list(map(int, input().strip().split()))
        out.append(t)

    return n, m, out

def makenew(rom):
    out=[]
    for line in rom:
        t=[]
        for item in line:
            t.append(item)
        out.append(t)
    return out

def blockSet(n, m, rom):

    for i in range(n):
        for j in range(m):
            if rom[i][j]==0:
                temp=makenew(rom)
                temp[i][j]=1
                bfs(temp, 1, 3, n, m)


def bfs(rom, now, limit, n, m):
    global count

    if now==limit:
        result=virus(rom, n, m)
        if count < result:
            count=result

    else:
        for i in range(n):
            for j in range(m):
                if rom[i][j]==0:
                    temp=makenew(rom)
                    temp[i][j]=1
                    bfs(temp, now+1, limit, n, m)

def virus(rom, n, m):

    vi=0
    for i in range(n):
        for j in range(m):
            if rom[i][j]==2:
                if i+1 < n:
                    if rom[i+1][j]==0:
                        rom[i+1][j]=2
                        goSpread(rom, i+1, j, n, m, vi)
                        #vi+=1
                if j+1 < m:
                    if rom[i][j+1]==0:
                        rom[i][j+1]=2
                        goSpread(rom, i, j+1, n, m, vi)
                        #vi += 1
                if i-1 >= 0:
                    if rom[i-1][j]==0:
                        rom[i-1][j]=2
                        goSpread(rom, i-1, j, n, m, vi)
                        #vi += 1
                if j-1 >= 0:
                    if rom[i][j-1]==0:
                        rom[i][j-1]=2
                        goSpread(rom, i, j-1, n, m, vi)
                        #vi += 1
    for i in range(n):
        for j in range(m):
            if rom[i][j]==0:
                vi+=1
    return vi


def goSpread(rom, i, j, n, m, vi):

    if i + 1 < n:
        if rom[i + 1][j] == 0:
            rom[i + 1][j] = 2
            goSpread(rom, i + 1, j, n, m, vi)
            #vi += 1
    if j + 1 < m:
        if rom[i][j + 1] == 0:
            rom[i][j + 1] = 2
            goSpread(rom, i, j + 1, n, m, vi)
            #vi += 1
    if i - 1 >= 0:
        if rom[i - 1][j] == 0:
            rom[i - 1][j] = 2
            goSpread(rom, i - 1, j, n, m, vi)
            #vi += 1
    if j - 1 >= 0:
        if rom[i][j - 1] == 0:
            rom[i][j - 1] = 2
            goSpread(rom, i, j - 1, n, m, vi)
            #vi += 1



if __name__=="__main__":
    n, m, rom=getInput()
    count=0

    blockSet(n, m, rom)
    print(count)