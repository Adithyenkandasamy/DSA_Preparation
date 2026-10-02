# MEX Game
# CodeChef Starters 258 - MEXGAME1

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * 105

    for x in a:
        freq[x] += 1

    mex = 0
    while freq[mex] > 0:
        mex += 1

    moves = 0

    for x in range(105):
        if x < mex:
            moves += x * (freq[x] - 1)
        elif x > mex:
            moves += (x - mex - 1) * freq[x]

    if moves % 2 == 1:
        print("Alice")
    else:
        print("Bob")
