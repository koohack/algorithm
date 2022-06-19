from collections import deque

def getInput():
    n = int(input())
    line = [list(input()) for _ in range(n)]
    return n, line

def sol(n, line):
    ## Mirror
    door = []

    for i in range(n):
        for j in range(n):
            if line[i][j] == "#": door.append([i, j])

    dp = line

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    checked = [[[0, 0, 0, 0] for i in range(n)] for _ in range(n)]

    q = deque()
    for i in range(4): q.append([door[0][0], door[0][1], i, 0])

    ## 0 down, 1 up, 2 rigth, 3 left
    mn = 9999999999999
    while q:
        x, y, dirc, num = q.popleft()

        x = x + dx[dirc]
        y = y + dy[dirc]
        if 0 <= x < n and 0 <= y < n:
            if x == door[-1][0] and y == door[-1][0]:
                if num < mn: mn = num
            elif dp[x][y] == '*': continue




if __name__ == "__main__":
    n, line = getInput()
    sol(n, line)