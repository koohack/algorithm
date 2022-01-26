import sys
from collections import deque
input = sys.stdin.readline

if __name__=="__main__":
    n, m=list(map(int, input().strip().split()))

    graph=[[] for i in range(n+1)]
    de=[0 for i in range(n+1)]

    queue=deque()
    answer=[]

    for i in range(m):
        a, b=list(map(int, input().strip().split()))
        graph[a].append(b)
        de[b]+=1

    for i in range(1, n+1):
        if de[i]==0:
            queue.append(i)

    while queue:
        temp= queue.popleft()
        answer.append(temp)
        for j in graph[temp]:
            de[j]-=1
            if de[j]==0:
                queue.append(j)

    print(*answer)