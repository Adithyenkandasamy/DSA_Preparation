# cook your dish here
def chef(n, arr):
    counts = {}

    for i in range(n):
        diff = arr[i] - i

        if diff in counts:
            counts[diff] += 1
        else:
            counts[diff] = 1

    max_frequent_staircase = max(counts.values())

    print(n - max_frequent_staircase)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    chef(n, arr)
