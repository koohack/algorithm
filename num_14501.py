
def getInput():
    n=int(input())

    day=[]
    cost=[]
    for i in range(n):
        a, b=list(map(int, input().strip().split()))
        day.append(a)
        cost.append(b)

    return n, day, cost

def dfs(check, pre, hap, day, cost, n):
    global answer
    if answer < hap:
        answer=hap

    for i in range(pre+1, n):
        payDay=day[i]
        pay=cost[i]
        if i+payDay > n:
            continue

        bk=0
        for j in range(i, i+payDay):
            if check[j]==1:
                bk=1
                break
            else:
                check[j]=1

        if not bk:
            dfs(check, i, hap+pay, day, cost, n)
            for j in range(i, i + payDay):
                check[j] = 0

def sol(n, day, cost):
    global answer
    check=[0]*n

    for i in range(n):
        payDay=day[i]
        pay=cost[i]
        if i+payDay > n:
            continue

        for j in range(i, i+payDay):
            check[j]=1
        dfs(check, i, pay, day, cost, n)
        for j in range(i, i+payDay):
            check[j]=0

    print(answer)





if __name__=="__main__":
    n, day, cost=getInput()
    answer=0
    sol(n, day, cost)