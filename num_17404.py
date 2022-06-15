def getInput():
    n = int(input())
    line = [list(map(int, input().strip().split())) for i in range(n)]
    return n, line

def sol(n, line):

    answer = 9999999999999999
    for init in range(3):
        dp = [[0] * 3 for _ in range(n)]

        for i in range(3):
            if i == init: dp[0][i] = line[0][i]
            else: dp[0][i] = 999999999999999

        for i in range(1, n):
            dp[i][0] = line[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = line[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = line[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        for i in range(3):
            if i != init:
                answer = min(answer, dp[-1][i])
    print(answer)


if __name__ == "__main__":
    n, line = getInput()
    sol(n, line)