# Chocolate Cutting

## Problem

We have an `N x M` chocolate bar.

We want to make one straight horizontal or vertical cut so that the two resulting pieces have exactly the same number of squares.

Determine whether this is possible.

## Input

The first line contains `T`, the number of test cases.

Each test case contains:

```text
N M
```

## Output

Print `Yes` if the chocolate can be divided into two equal pieces. Otherwise print `No`.

## Example

### Input
```text
3
2 5
3 3
4 7
```

### Output
```text
Yes
No
Yes
```

## Idea

The chocolate contains `N * M` squares.

For two pieces to be equal, the total number of squares must be even.

So we only need to check:

```text
N * M % 2 == 0
```

If it is even, at least one of `N` or `M` is even, so we can cut through the middle.

## Complexity

- Time: `O(1)` per test case
- Space: `O(1)`
