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

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    checked = [[[-1, -1, -1, -1] for i in range(n)] for _ in range(n)]

    q = deque()
    for i in range(4):
        q.append([door[0][0], door[0][1], i])
        checked[door[0][0]][door[0][1]][i] = 0

    mn = 9999999999999999999
    while q:
        x, y, dirc = q.popleft()

        if x == door[1][0] and y == door[1][1]:
            if mn > checked[x][y][dirc]: mn = checked[x][y][dirc]

        nx = x + dx[dirc]
        ny = y + dy[dirc]

        if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] != '*':
            if checked[nx][ny][dirc] == -1 or checked[nx][ny][dirc] > checked[x][y][dirc]:
                checked[nx][ny][dirc] = checked[x][y][dirc]
                q.append([nx, ny, dirc])
            if dp[nx][ny] == '!':
                if dirc < 2:
                    for d in range(2, 4):
                        if checked[nx][ny][d] == -1 or checked[nx][ny][d] > checked[x][y][dirc]+1:
                            checked[nx][ny][d] = checked[x][y][dirc] + 1
                            q.append([nx, ny, d])
                else:
                    for d in range(2):
                        if checked[nx][ny][d] == -1 or checked[nx][ny][d] > checked[x][y][dirc]+1:
                            checked[nx][ny][d] = checked[x][y][dirc] + 1
                            q.append([nx, ny, d])
    print(mn)

if __name__ == "__main__":
    n, line = getInput()
    sol(n, line)