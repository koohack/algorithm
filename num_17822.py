from collections import deque

def getInput():
    n, m, t = list(map(int, input().strip().split()))
    pan = [deque(map(int, input().strip().split())) for _ in range(n)]
    cmd = [list(map(int, input().strip().split())) for _ in range(t)]
    return n, m, t, pan, cmd

def rotate(pan, num, rclockwise, runCount):

    for i, line in enumerate(pan):
        if not (i+1) % num:
            if not rclockwise:
                for _ in range(runCount):
                    temp = line.pop()
                    line.insert(0, temp)
            else:
                for _ in range(runCount):
                    temp = line.popleft()
                    line.append(temp)

def checkSame(pan, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    store = [[0]*m for _ in range(n)]

    checker = 0
    for i in range(n):
        for j in range(m):
            if pan[i][j] == -1: continue

            ##상하좌우 체크
            flag = 0
            for z in range(4):
                x = i + dx[z]
                y = j + dy[z]

                if 0 <= x < n and 0 <= y < m:
                    if pan[i][j] == pan[x][y]:
                        store[x][y] = 1
                        flag = 1
                        checker = 1


            ## j = 0 or m-1
            if j == 0:
                if pan[i][j] == pan[i][m-1]:
                    store[i][m-1] = 1
                    flag = 1
                    checker = 1
            if j == m-1:
                if pan[i][j] == pan[i][0]:
                    store[i][0] = 1
                    flag = 1
                    checker = 1

            if flag: store[i][j] = 1

    if not checker: noChange(pan, n, m)
    else:
        for i in range(n):
            for j in range(m):
                if store[i][j]:
                    pan[i][j] = -1


def noChange(pan, n, m):
    total = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if pan[i][j] > 0:
                count += 1
                total += pan[i][j]

    if count == 0: return
    check = total / count

    for i in range(n):
        for j in range(m):
            if pan[i][j] > 0:
                if pan[i][j] > check: pan[i][j] -= 1
                elif pan[i][j] < check: pan[i][j] += 1


def sol(n, m, t, pan, cmd):

    for num, rclockwise, runCount in cmd:
        rotate(pan, num, rclockwise, runCount)
        #print(pan)
        checkSame(pan, n, m)
        #print(pan)
        #print("-------------")

    answer = 0
    for i in range(n):
        for j in range(m):
            if pan[i][j] > 0:
                answer += pan[i][j]
    print(answer)

if __name__ == "__main__":
    n, m, t, pan, cmd = getInput()
    sol(n, m, t, pan, cmd)