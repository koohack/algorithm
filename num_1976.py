from collections import deque

def getInput():
    n = int(input())
    m = int(input())
    dp = [list(map(int, input().strip().split())) for i in range(n)]
    city = list(map(int, input().strip().split()))
    return n, m, dp, city

def find(check):
    for i, item in enumerate(check):
        if not item: return i
    return -1

def sol(n, m, dp, city):
    check = [[] for i in range(n)]

    ## make graph
    for i in range(n):
        for j in range(i+1, n):
            if dp[i][j] == 1:
                check[i].append(j)
                check[j].append(i)

    ## find connected
    count = 0
    num = 1
    visited = [0] * n
    while count < n:
        start = find(visited)
        if start==-1: break

        q = deque()
        q.append(start)

        while q:
            now = q.popleft()
            visited[now] = num
            canmove = check[now]

            for item in canmove:
                if not visited[item]:
                    q.append(item)
                    count += 1
        num += 1

    me = visited[city[0]-1]
    for i in city:
        if visited[i-1] != me: return False
    return True

if __name__ == "__main__":
    n, m, dp, city = getInput()
    answer = sol(n, m, dp, city)
    if answer: print("YES")
    else: print("NO")