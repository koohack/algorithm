
def deprint(de):
    for i in de:
        print(i)

def change(de):
    out=[]
    for line in de:
        t=[]
        for i in line:
            t.append(int(i))
        out.append(t)
    return out

def rotate(d, num):
    line=de[num]
    if d==1:
        temp=line.pop()
        line.insert(0, temp)
    else:
        temp=line.pop(0)
        line.append(temp)

def right(num, d):
    if num+1 <= 4 and de[num+1][6]!=de[num][2]:
        right(num+1, -d)
    rotate(d, num)


def left(num, d):
    if num-1 >= 1 and de[num-1][2]!=de[num][6]:
        left(num-1, -d)
    rotate(d, num)

def sol():

    for num, d in cmd:

        if num+1 <= 4 and de[num+1][6]!=de[num][2]:
            right(num+1, -d)
        if num - 1 >= 1 and de[num - 1][2] != de[num][6]:
            left(num - 1, -d)
        rotate(d, num)
        #deprint(de)

    hap=0
    if de[1][0]==1:
        hap+=1
    if de[2][0]==1:
        hap+=2
    if de[3][0]==1:
        hap+=4
    if de[4][0]==1:
        hap+=8
    print(hap)

de=[list(input()) for _ in range(4)]
de=change(de)
de.insert(0, [])

n=int(input())
cmd=[list(map(int, input().strip().split())) for i in range(n)]

sol()