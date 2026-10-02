# SANDWICH7

## Problem

A sandwich needs:
- 2 slices of bread
- 1 slice of ham or 1 slice of cheese

We are given `B` bread slices, `H` ham slices and `C` cheese slices.

Find the maximum number of sandwiches we can make.

## Input

One line containing three integers:

```text
B H C
```

## Output

Print the maximum number of sandwiches.

## Example

### Input
```text
7 2 3
```

### Output
```text
3
```

## Idea

One sandwich needs 2 breads, so the number of sandwiches possible using bread is:

```text
B // 2
```

For the filling, we can use either ham or cheese, so we have:

```text
H + C
```

Both conditions have to be satisfied. So we take the smaller value.

```text
answer = min(B // 2, H + C)
```

## Complexity

- Time: `O(1)`
- Space: `O(1)`
