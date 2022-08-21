def getInput():
    r, c, m = list(map(int, input().strip().split()))
    sharks = [list(map(int, input().strip().split())) for _ in range(m)]

    return r, c, m, sharks

def sol(r, c, m, sharks):
    pl = [[[] for t in range(c)] for _ in range(r)]
    answer = 0

    if m == 0:
        print(0)
        return

    for i in range(len(sharks)):
        sharks[i][0] -= 1
        sharks[i][1] -= 1

        x, y, s, d, z = sharks[i]
        pl[x][y].append([s,d,z])

    for king in range(c):

        ## get fish
        for index in range(r):
            if pl[index][king]:
                ate = pl[index][king].pop()
                answer += ate[2]
                break

        ## move the shark
        store = []
        for i in range(r):
            for j in range(c):
                if pl[i][j]:
                    s, d, z = pl[i][j].pop()

                    tr = r - 1
                    tc = c - 1

                    if d == 1:
                        canMove = s % ((r-1)*2)

                        ## change to down
                        if i - canMove <= 0:
                            canMove = canMove - i

                            ## return to up
                            if tr - canMove <= 0:
                                canMove = canMove - tr
                                store.append([tr - canMove, j, s, d, z])
                            ## just down
                            else:
                                store.append([canMove, j, s, 2, z])
                        else:
                            store.append([i-canMove, j, s, d, z])

                    elif d == 2:
                        canMove = s % ((r-1)*2)

                        ## change to up
                        if tr - i - canMove <= 0:
                            canMove = canMove - tr + i

                            ## return to down
                            if tr - canMove <= 0:
                                canMove = canMove - tr
                                store.append([canMove, j, s, d, z])
                            else:
                                store.append([tr - canMove, j, s, 1, z])
                        else:
                            store.append([i+canMove, j, s, d, z])

                    elif d == 3:
                        canMove = s % ((c-1)*2)

                        ## change to left
                        if tc - j - canMove <= 0:
                            canMove = canMove - tc + j

                            ## return to right
                            if tc - canMove <= 0:
                                canMove = canMove - tc
                                store.append([i, canMove, s, d, z])
                            else:
                                store.append([i, tc - canMove, s, 4, z])
                        else:
                            store.append([i, j+canMove, s, d, z])


                    else:
                        canMove = s % ((c-1)*2)

                        ## change to right
                        if j - canMove <= 0:
                            canMove = canMove - j

                            ## return to left
                            if tc - canMove <= 0:
                                canMove = canMove - tc
                                store.append([i, tc - canMove, s, d, z])
                            else:
                                store.append([i, canMove, s, 3, z])
                        else:
                            store.append([i, j - canMove, s, d, z])

        ## mapping the shark
        for shark in store:
            x, y, s, d, z = shark
            pl[x][y].append([s,d,z])

        ## remove more than 2
        for i in range(r):
            for j in range(c):
                if len(pl[i][j]) > 1:
                    mx = [0, 0, 0]
                    while pl[i][j]:
                        temp = pl[i][j].pop()
                        if temp[2] > mx[2]:
                            mx = temp
                    pl[i][j].append(mx)

        #for a in pl:
         #   print(a)
        #print("-----------")

    print(answer)
    return





if __name__ == "__main__":
    r, c, m, sharks = getInput()
    sol(r, c, m, sharks)