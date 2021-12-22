mn=9999999999999999

def getInput():
    out=[]
    num=int(input())
    for i in range(num):
        inp=list(map(int, input().strip().split()))
        out.append(inp)
    return out

def sol1(rgb):
    for i in range(1, len(rgb)):
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2])+rgb[i][0]
        rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2])+rgb[i][1]
        rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1])+rgb[i][2]
    return(min(rgb[len(rgb)-1]))
'''''
def sol(rgb, pre, now, limit, hap):
    global mn

    if now==limit:
        if hap < mn:
            mn=hap
    else:
        for i, item in enumerate(rgb[now]):
            temp = hap
            if i != pre:
                temp+=item
                sol(rgb, i, now+1, limit, temp)
'''''

if __name__=="__main__":
    rgb=getInput()
    #sol(rgb, -1, 0, len(rgb), 0)
    print(sol1(rgb))
