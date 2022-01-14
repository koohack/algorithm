import sys
import heapq
input = sys.stdin.readline

v, e = list(map(int, input().strip().split()))
startNum = int(input())

out = [[] for _ in range(v + 1)]
for i in range(e):
    u, z, w = list(map(int, input().strip().split()))
    out[u].append((z, w))



def sol(v, e, startNum, line):
    visit = [0] * (v + 1)
    m = [0] * (v + 1)

    for item in line:
        if startNum == item[0]:
            visit[item[1]] = 1
            m[item[1]] = m[item[0]] + item[2]
            bfs(item[1], visit, m, line)

    return m


def bfs(now, visit, m, line):
    for item in line:
        if item[0] == now:
            if m[item[0]] + item[2] < m[item[1]] or m[item[1]] == 0:
                m[item[1]] = m[item[0]] + item[2]
                bfs(item[1], visit, m, line)
            else:
                continue


def getAnswer(me, line):
    for i, item in enumerate(line):
        if i == 0:
            continue
        if i != me and item == 9999999999:
            print("INF")
        else:
            print(item)


def sol1(v, e, startNum, line):
    m = [9999999999] * (v + 1)

    q = []
    heapq.heappush(q, (0, startNum))
    m[startNum]=0
    while q:
        dist, now = heapq.heappop(q)

        if m[now] < dist:
            continue

        for i in line[now]:
            cost=dist+i[1]

            if cost < m[i[0]]:
                m[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

    return m

if __name__ == "__main__":
    answer = sol1(v, e, startNum, out)
    getAnswer(startNum, answer)
