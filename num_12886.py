from collections import deque

def getInput():
    line = list(map(int, input().strip().split()))
    return line

def sol(line):
    hap = sum(line)
    if hap % len(line): return 0

    visited = [[0] * 1501 for i in range(1501)]
    a, b, c = line

    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        a, b = q.popleft()
        c = hap - a - b

        if a==b==c: return 1

        for na, nb in ((a, b), (a, c), (b, c)):
            if na > nb and na - nb > 0:
                na -= nb
                nb += nb
            elif na < nb and nb - na > 0:
                nb -= na
                na += na
            else: continue
            nc = hap - na - nb
            a = min(min(na, nb), nc)
            b = max(max(na, nb), nc)
            if not visited[a][b]:
                q.append((a, b))
                visited[a][b] = 1
    return 0

if __name__ == "__main__":
    line = getInput()
    answer = sol(line)
    print(answer)