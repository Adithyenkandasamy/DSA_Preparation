# cook your dish here
def chef(n, mset, k):
    seats = []
    i = 1

    while len(seats) < k:
        if i not in mset:
            seats.append(i)
            mset[i] = 1
        i += 1

    print(*seats)

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    mset = {int(x): 1 for x in input().split()}
    chef(n, mset, k)
