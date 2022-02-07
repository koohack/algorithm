import heapq, sys
input = sys.stdin.readline

def sol():
    n=int(input())

    left=[]
    right=[]

    for i in range(n):
        num=int(input())

        if len(left)==len(right):
            heapq.heappush(left, (-num, num))
        else:
            heapq.heappush(right, (num, num))

        if right and left[0][1] > right[0][1]:
            min=heapq.heappop(right)[1]
            max=heapq.heappop(left)[1]
            heapq.heappush(left, (-min, min))
            heapq.heappush(right, (max, max))

        print(left[0][1])



if __name__=="__main__":
    sol()