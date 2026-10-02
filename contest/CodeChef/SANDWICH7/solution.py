# cook your dish here
def chef(b, h, c):
    bread = b // 2
    filling = h + c
    print(min(bread, filling))

b, h, c = map(int, input().split())
chef(b, h, c)
