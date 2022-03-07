from collections import deque

def getInput():
    n, m, k=list(map(int, input().strip().split()))
    dp=[list(map(int, input().strip().split())) for i in range(n)]

    tree=[[deque() for a in range(n)] for b in range(n)]
    for _ in range(m):
        a, b, c=list(map(int, input().strip().split()))
        tree[a-1][b-1].append(c)

    return dp, k, tree

def sol(dp, count, tree):
    n=len(dp)
    tu=[[5]*n for i in range(n)]
    dx=[1, -1, 0, 0, 1, 1, -1, -1]
    dy=[0, 0, 1, -1, 1, -1, 1, -1]

    for _ in range(count):
        # 봄 여름 함께
        for i in range(n):
            for j in range(n):
                length=len(tree[i][j])
                for k in range(length):
                    if tree[i][j][k] <= tu[i][j]:
                        tu[i][j]-=tree[i][j][k]
                        tree[i][j][k]+=1
                    else:
                        for _ in range(k, length):
                            tu[i][j]+=tree[i][j].pop()//2
                        break
        # 가을 겨울
        for i in range(n):
            for j in range(n):
                for k in tree[i][j]:
                    if k % 5 == 0:
                        for z in range(8):
                            x=i+dx[z]
                            y=j+dy[z]
                            if 0<=x<n and 0<=y<n:
                                tree[x][y].appendleft(1)
                tu[i][j]+=dp[i][j]
    return tree

if __name__=="__main__":
    dp, k, tree=getInput()
    tree=sol(dp, k, tree)
    count=0
    for i in range(len(dp)):
        for j in range(len(dp)):
            count+=len(tree[i][j])
    print(count)