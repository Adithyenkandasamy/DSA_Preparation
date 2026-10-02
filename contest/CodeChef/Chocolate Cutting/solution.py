# cook your dish here
def chef(n, m):
    result = n * m
    print("Yes" if result % 2 == 0 else "No")

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    chef(n, m)
