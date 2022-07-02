from collections import deque

def getInput():
    n, m, v = list(map(int, input().strip().split()))
    line = [list(map(int, input().strip().split())) for i in range(m)]
    return n, m, v, line

def prt(line):
    st = ''
    for i in line:
        st += str(i) + ' '
    return st

def sol(n, m, v, line):
    tree = [[] for i in range(n+1)]
    for a, b in line:
        tree[a].append(b)
        tree[b].append(a)

    for items in tree:
        items.sort()

    dfs = []
    bfs = []

    check = [0] * (n+1)
    check[v] = 1
    dfs.append(v)
    DFS(v, tree, check, dfs)

    print(prt(dfs))

    check = [0] * (n+1)
    check[v] = 1
    bfs.append(v)
    BFS(v, tree, check, bfs)
    print(prt(bfs))

def DFS(start, tree, check, store):
    now = tree[start]

    for i in range(len(now)):
        if not check[now[i]]:
            check[now[i]] = 1
            store.append(now[i])
            DFS(now[i], tree, check, store)

def BFS(start, tree, check, store):
    q = deque()
    q.append(start)

    while q:
        num = q.popleft()
        now = tree[num]

        for item in now:
            if not check[item]:
                check[item] = 1
                store.append(item)
                q.append(item)

if __name__ == "__main__":
    n, m, v, line = getInput()
    sol(n, m, v, line)