# Shuffle Easy - SHUFFLEEZ
MOD = 998244353

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    _ = list(map(int, input().split()))  # permutation, not needed directly

    answer = 1
    remaining = k - 1

    for i in range(1, n + 1):
        if i + k - 1 <= n:
            remaining += 1

        answer = (answer * remaining) % MOD
        remaining -= 1

    print(answer)
