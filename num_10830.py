import copy

def getInput():
    n, b=list(map(int, input().strip().split()))
    mat=[list(map(int, input().strip().split())) for i in range(n)]
    return n, b, mat

def mul(mat, mat1, n):
    new = []
    for first in range(n):
        temp = []
        for second in range(n):
            hap = 0
            for i in range(n):
                hap += mat[first][i] * mat1[i][second]
            temp.append(hap % 1000)
        new.append(temp)

    return new

def sol(n, b, mat):
    check=bin(b)[2:]

    result=[[1 if i==j else 0 for i in range(n)] for j in range(n)]

    for i in range(len(check)-1, -1, -1):
        if check[i]=='1':
            result=mul(result, mat, n)
        mat=mul(mat, mat, n)

    for line in result:
        print(*line)




if __name__=="__main__":
    n, b, mat=getInput()
    sol(n, b, mat)