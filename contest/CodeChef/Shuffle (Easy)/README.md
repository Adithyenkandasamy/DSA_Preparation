# Shuffle - Easy (SHUFFLEEZ)

## Problem

We are given a permutation `P` of size `N` and an integer `K`.

For every possible starting position, we sort the next `K` elements in ascending order.

After doing all these operations, we want the final array to become:

```text
[1, 2, 3, ..., N]
```

Count how many starting permutations can produce this final sorted array.

## Input

Each test case contains:

```text
N K
```

followed by a permutation of `1` to `N`.

## Output

Print the number of valid permutations modulo:

```text
998244353
```

## Idea

Think about where the value `1` can initially be.

It has to be inside the first `K` positions, because the first operation is the only way to move it to position `1`.

So there are `K` choices.

After fixing `1`, look at `2`. It can be placed in the next valid range, giving another number of choices.

The same idea continues for every value.

For value `i`, the number of available positions is:

```text
min(N, i + K - 1) - (i - 1)
```

Multiply all these choices together.

## Complexity

- Time: `O(N)` per test case
- Space: `O(1)` apart from the input permutation
