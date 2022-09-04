def getInput():
    n = int(input())
    line = list(map(int, input().strip().split()))
    return n, line

def sol(n, line):

    answer = 0

    dp = [[0]*(n) for _ in range(n)]

    store = [0 for i in range(n+1)]
    store[0] = line[0]
    for i in range(1, n):
        store[i] = store[i-1] + line[i]
    store = [0] + store

    for gap in range(1, n):
        for i in range(n-gap):
            mn = min(dp[i][i+k] + dp[i+k+1][i+gap] for k in range(gap))
            dp[i][i+gap] = mn + store[i+gap+1] - store[i]
            #print(mn)
            '''''
            print()
            for i in dp:
                print(i)
        print("---------")
        '''''
    answer = dp[0][n-1]
    return answer

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        n, line = getInput()
        answer = sol(n, line)
        print(answer)