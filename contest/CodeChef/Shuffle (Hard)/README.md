# Shuffle - Hard (SHUFFLEHD)

## Problem

We are given:
- `N`
- `K`
- a target permutation `Q`

The same shuffle operation is performed: every length-`K` subarray is sorted in place.

We need to count how many permutations `P` can become exactly `Q`.

The answer is printed modulo `998244353`.

## Input

For each test case:

```text
N K
Q1 Q2 ... QN
```

## Output

Print the number of possible starting permutations.

## Idea

We process the target array from left to right.

For the first value, it has to come from the first `K` positions.

For every next value, we look at the range of positions from which it can reach its target position.

If the current value is greater than every value seen before, it can be placed in any currently available position in that range.

If it is not a new maximum, it is forced to one particular position.

If that forced position is outside the array, the answer becomes `0`.

We multiply the number of choices for each value.

## Complexity

- Time: `O(N)` per test case
- Space: `O(N)` for the input
