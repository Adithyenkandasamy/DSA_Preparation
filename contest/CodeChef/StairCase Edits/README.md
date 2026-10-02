# StairCase Edits

## Problem

We are given an array `A`.

We need to replace the minimum number of elements so that:

```text
A[i] - A[i-1] = 1
```

for every valid `i`.

In other words, the final array should increase by exactly `1` at every step.

## Input

The first line contains `T`.

For each test case:
- first line: `N`
- second line: `N` integers

## Output

Print the minimum number of replacements needed.

## Example

### Input
```text
2
5
3 4 5 9 7
4
5 6 7 8
```

### Output
```text
2
0
```

## Idea

For a perfect staircase:

```text
A[i] = A[0] + i
```

So:

```text
A[i] - i
```

must be the same for all elements that we keep unchanged.

Therefore, I calculate `A[i] - i` for every position and count how many times each value occurs.

The value occurring the most tells us the largest number of elements we can keep.

So:

```text
answer = N - maximum_frequency
```

## Complexity

- Time: `O(N)` average using a dictionary
- Space: `O(N)`
