# MEX Game

## Problem

Alice and Bob play a game on an array.

They take turns reducing an element by `1`, but a move is allowed only when the MEX of the array does not change.

The player who cannot make a valid move loses.

Find who wins when both players play optimally.

## Input

The first line contains `T`.

For each test case:
- first line: `N`
- second line: `N` integers

## Output

Print:

```text
Alice
```

if Alice wins, otherwise print:

```text
Bob
```

## Example

### Input
```text
2
3
0 1 3
3
0 1 2
```

### Output
```text
Bob
Bob
```

## Idea

First find the MEX of the array.

Let it be `M`.

For values greater than `M`, they can keep getting reduced until they become `M + 1`.

For values smaller than `M`, we can reduce all extra copies to `0`. We cannot remove the last required copy of a value below `M`, because then the MEX would change.

So the total number of possible moves is fixed.

The useful formula is:

```text
for x < M:
    moves += x * (freq[x] - 1)

for x > M:
    moves += (x - M - 1) * freq[x]
```

If the total number of moves is odd, Alice makes the last move.

Otherwise Bob makes the last move.

## Complexity

- Time: `O(N + max(A))`
- Space: `O(max(A))`
