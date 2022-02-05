import copy, sys
input = sys.stdin.readline

def first():
    n, k = list(map(int, input().strip().split()))
    w = []
    v = []
    for i in range(n):
        we, ve = list(map(int, input().strip().split()))
        w.append(we)
        v.append(ve)
    w=w
    v=v

    dp = [0 for _ in range(k+1)]

    for i in range(n):
        weight = w[i]
        value = v[i]
        for j in range(k, weight-1, -1):
            dp[j] = max(dp[j - weight] + value, dp[j])

    print(dp[-1])

if __name__=="__main__":
    first()

