# Find All Palindromes

**Topic:** Two Pointers  
**Difficulty:** Easy  
**Language:** Python 3  
**Pattern:** Two Pointers + String Normalization

## Problem

Given an array of usernames, return all usernames that are palindromes.

A palindrome is a string that reads the same forwards and backwards.

The comparison must be case-insensitive, meaning uppercase and lowercase letters are treated as equal.

### Examples

**Example 1**

```python
usernames = [
    "Tricer66",
    "TREXerT",
    "Veloc1COLEv",
    "stego95"
]

Output:
["TREXerT", "Veloc1COLEv"]
```

**Example 2**

```python
usernames = ["nigersaurus111", "BRACHI33"]

Output:
[]
```

## Approach: Two Pointers

Use two pointers to compare characters from opposite ends of each username.

### Algorithm

1. Create an empty list called `result` to store palindrome usernames.
2. Iterate through every username in the input array.
3. Convert the current username to lowercase to make the comparison case-insensitive.
4. Initialize two pointers:
   - `left = 0`: points to the first character.
   - `right = len(username) - 1`: points to the last character.
5. Compare the characters at both pointers.
6. If the characters are different, the username is not a palindrome. Stop checking that username.
7. If they match, move `left` one position forward and `right` one position backward.
8. Continue until the pointers meet or cross.
9. If all comparisons match, append the original username to `result`.
10. Return `result`.

## Complexity Analysis

Let:

- `n` = number of usernames.
- `m` = maximum length of a username.

### Time Complexity: O(n × m)

- We iterate through all `n` usernames.
- For each username, the two-pointer algorithm performs at most `m / 2` comparisons.
- Therefore, the overall time complexity is O(n × m).

### Auxiliary Space Complexity: O(m)

- Converting each username to lowercase creates a normalized string.
- The two pointers and boolean variable require constant space.
- The normalized string requires O(m) space.
- Therefore, auxiliary space complexity is O(m), excluding the output list.

The output list requires O(k) additional references, where `k` is the number of palindromes returned.

## Testing

Run the tests from the repository root:

```bash
python3 -m unittest discover -s 02-two-pointers/find_all_palindromes -p "test_*.py" -v
```

Test cases include:

- Both provided examples.
- Mixed uppercase and lowercase characters.
- Empty input.
- Single-character usernames.
- All usernames are palindromes.
- No usernames are palindromes.

## Key Learnings

- Practiced the Two Pointers algorithm.
- Learned to normalize strings using `lower()`.
- Used string indexing without converting strings into character lists.
- Practiced breaking out of a loop when a mismatch is found.
- Learned to write unit tests using Python's `unittest` framework.
- Analyzed time and auxiliary space complexity.
