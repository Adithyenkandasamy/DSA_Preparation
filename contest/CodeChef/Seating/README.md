# Seating

## Problem

There are `N` seats numbered from `1` to `N`.

Some seats are already occupied. Then `K` more people enter one by one.

Every person always takes the lowest numbered seat that is still empty.

Print the seats taken by the `K` new people.

## Input

The first line contains `T`.

For each test case:

```text
N M K
```

The next line contains `M` already occupied seat numbers.

## Output

Print the `K` seats occupied by the new people.

## Example

### Input
```text
1
7 2 3
2 5
```

### Output
```text
1 3 4
```

## Idea

I keep the already occupied seats in a set.

Then I start checking seats from `1`.

Whenever the seat is not in the set:
1. add it to the answer
2. mark it as occupied
3. continue until `K` seats are found

## Complexity

The simple simulation used here checks seats from the beginning, so its worst-case time can be `O(NK)`.

Space: `O(N)`.
