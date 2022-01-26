import sys
from collections import deque
#input = sys.stdin.readline



def getInput():
    n=int(input())
    m=int(input())
    return n, m

if __name__=="__main__":
    n, m=getInput()

    graph=[[] for i in range(n+1)]
    visit=[0 for i in range(n+1)]
    m=[0 for i in range(n+1)]

    for i in range(m):
        a, b, c=list(map(int, input().strip().split()))
        graph[a].append((b,c))
        graph[b].append((a,c))

    q=deque()
    for i, item in enumerate(graph[1]):
        m[item[0]]+=item[1]
        q.append(item[0])

    while q:
        temp=q.popleft()

        if not visit[temp]:








