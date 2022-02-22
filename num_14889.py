
def getInput():
    n=int(input())
    m=[list(map(int, input().strip().split())) for i in range(n)]

    return n, m

def sol(n, m):

    check=[0]*n

    for i in range(n):
        check[i]=1
        dfs(check, i, 1, int(n/2), m)
        check[i]=0


def getHap(check, m):
    first=[]
    second=[]

    for i, item in enumerate(check):
        if item:
            first.append(i)
        else:
            second.append(i)
    hap1=0
    for i in range(len(first)):
        for j in range(i+1, len(first)):
            hap1+=m[first[i]][first[j]]
            hap1+=m[first[j]][first[i]]
    hap2=0
    for i in range(len(second)):
        for j in range(i+1, len(second)):
            hap2+=m[second[i]][second[j]]
            hap2+=m[second[j]][second[i]]
    if hap1 > hap2:
        return hap1-hap2
    else:
        return hap2-hap1


def dfs(check, pre, now, limit, m):
    global answer

    if now==limit:
        temp=getHap(check, m)
        if temp < answer:
            answer=temp
    else:
        for i in range(pre+1, len(m)):
            if check[i]==0:
                check[i]=1
                dfs(check, i, now+1, limit, m)
                check[i]=0

if __name__=="__main__":
    answer=9999999999
    n, m=getInput()
    sol(n, m)
    print(answer)