from collections import deque

line = []
mn = 999999999
c = 999999999
space = 0

def getInput():
    n, m = list(map(int, input().strip().split()))
    line = [list(map(int, input().strip().split())) for i in range(n)]
    return n, m, line

def spread(xijun, check):
    global mn, space

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dp = [[0]*len(line) for _ in range(len(line))]
    n = len(line)

    count = 0
    for i in range(len(line)):
        for j in range(len(line[0])):
            if line[i][j] == 1:
                dp[i][j] = -2
            elif line[i][j] == 0:
                count += 1

    ## xijun list
    live = deque()
    for i, item in enumerate(check):
        if item:
            dp[xijun[i][0]][xijun[i][1]] = 1
            live.append([xijun[i][0], xijun[i][1]])
        else: dp[xijun[i][0]][xijun[i][1]] = -1

    ## spread
    while live:
        if count == 0: break
        x, y = live.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if line[nx][ny] == 1:
                    continue

                if not dp[nx][ny]:
                    dp[nx][ny] = dp[x][y] + 1
                    live.append([nx, ny])
                    count -= 1
                elif dp[nx][ny] == -1:
                    dp[nx][ny] = dp[x][y] + 1
                    live.append([nx, ny])

                if count == 0: break
        if count == 0:break

    #for z in dp:
     #   print(z)
    #print("-------")

    nowmx = 0
    flag = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                nowmx = 999999999
                flag = 1
                break
            if dp[i][j] > nowmx: nowmx = dp[i][j]
        if flag: break
    #print(nowmx)
    if mn > nowmx: mn = nowmx

def dfs(xijun, check, prei, now, limit):
    if now == limit:
        spread(xijun, check)
        return
    else:
        for i in range(prei+1, len(xijun)):
            if not check[i]:
                check[i] = 1
                dfs(xijun, check, i, now+1, limit)
                check[i] = 0


def sol(n, m, line):
    ## check num space
    xijun = []
    for i in range(n):
        for j in range(n):
            if line[i][j] == 2: xijun.append([i, j])

    check = [0] * len(xijun)

    for i in range(len(xijun)):
        check[i] = 1
        dfs(xijun, check, i, 1, m)
        check[i] = 0

    if mn == c: print(-1)
    else: print(mn-1)

if __name__ == "__main__":
    n, m, line = getInput()
    sol(n, m, line)
