# Shuffle Hard - SHUFFLEHD
MOD = 998244353

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))

    answer = 1
    remaining = k - 1
    current_max = 0

    for i in range(1, n + 1):
        if i + k - 1 <= n:
            remaining += 1

        if q[i - 1] > current_max:
            answer = (answer * remaining) % MOD
            current_max = q[i - 1]
        elif i + k - 1 > n:
            answer = 0

        remaining -= 1

    print(answer)
