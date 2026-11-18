# Day 01 – Get Age Range

**Topic:** Arrays  
**Difficulty:** Beginner  
**Language:** Python

## Problem Statement

Given an array of dinosaur ages, calculate the age range of the population.

The age range is the difference between the maximum age and minimum age.

**Formula:**

```text
Age Range = Maximum Age - Minimum Age
```

### Examples

**Example 1**

```python
ages = [8, 51, 3, 64, 1, 75, 9, 100]

Output: 99
```

Explanation:

- Maximum age = 100
- Minimum age = 1
- Age range = 100 - 1 = 99

**Example 2**

```python
ages = [8, 2, 5, 12, 3]

Output: 10
```

Explanation:

- Maximum age = 12
- Minimum age = 2
- Age range = 12 - 2 = 10

## Algorithm

**Input:** An array of ages  
**Output:** The difference between the maximum and minimum ages.

### Steps

1. Initialize `max_age` with the first element of the array.
2. Initialize `min_age` with the first element of the array.
3. Iterate through every element in the array.
4. If the current age is greater than `max_age`, update `max_age`.
5. If the current age is smaller than `min_age`, update `min_age`.
6. Subtract `min_age` from `max_age`.
7. Return the calculated age range.

## Python Implementation

```python
def get_age_range(ages):
    max_age = ages[0]
    min_age = ages[0]

    for age in ages:
        if age > max_age:
            max_age = age

        if age < min_age:
            min_age = age

    return max_age - min_age
```

## Test Cases

| Input                           | Expected Output |
| ------------------------------- | --------------: |
| `[8, 51, 3, 64, 1, 75, 9, 100]` |              99 |
| `[8, 2, 5, 12, 3]`              |              10 |
| `[5, 10]`                       |               5 |
| `[5, 5]`                        |               0 |
| `[5]`                           |               0 |

All five test cases should pass.

## Complexity Analysis

### Time Complexity: O(n)

- The algorithm traverses the array once.
- Each element is checked against the current maximum and minimum.
- If the array contains n elements, the algorithm performs a linear number of operations.

### Auxiliary Space Complexity: O(1)

- Only two variables are maintained: `max_age` and `min_age`.
- No additional array or data structure is created.
- The extra space remains constant regardless of input size.

## Key Concepts Learned

- Array traversal using Python `for` loops.
- Initializing variables using the first array element.
- Comparing values using conditional statements.
- Finding minimum and maximum values.
- Writing reusable functions.
- Understanding time and space complexity.
- Handling edge cases such as single-element and equal-element arrays.

## What I Learned

I learned how to traverse an array and maintain two variables to track its minimum and maximum values.

I also learned why initializing these variables with the first element of the array is safer than initializing them with zero, particularly when working with negative numbers.
