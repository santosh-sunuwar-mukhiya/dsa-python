"""
Problem: Find All Palindromes
Topic: Two Pointers
Difficulty: Beginner

Description:
Given an array of usernames, return all usernames
that are palindromes, ignoring letter case.

A palindrome is a string that reads the same
forwards and backwards.

Time Complexity: O(n * m)
Space Complexity: O(m) auxiliary space, excluding output
"""


def find_all_palindromes(usernames):

    # Step 1: Initialize an empty list to store palindrome usernames.
    result = []

    # Step 2: Iterate through every username.
    for username in usernames:

        # Step 3: Convert the username to lowercase.
        normalized_username = username.lower()

        # Step 4: Initialize two pointers.
        left = 0
        right = len(normalized_username) - 1

        is_palindrome = True

        # Step 5: Compare characters from both ends.
        while left < right:

            # Step 6: If characters don't match, it is not a palindrome.
            if normalized_username[left] != normalized_username[right]:
                is_palindrome = False
                break

            # Step 7: Move both pointers towards the center.
            left += 1
            right -= 1

        # Step 8: Store the original username if it is a palindrome.
        if is_palindrome:
            result.append(username)

    # Step 9: Return all palindrome usernames.
    return result


if __name__ == "__main__":

    # Example 1
    print(
        find_all_palindromes(
            ["Tricer66", "TREXerT", "Veloc1COLEv", "stego95"]
        )
    )
    # Expected: ["TREXerT", "Veloc1COLEv"]

    # Example 2
    print(
        find_all_palindromes(["nigersaurus111", "BRACHI33"])
    )
    # Expected: []

    # Example 3: Mixed uppercase and lowercase.
    print(
        find_all_palindromes(["Bob", "zAAaaZ"])
    )
    # Expected: ["Bob", "zAAaaZ"]

    # Example 4: Empty array.
    print(find_all_palindromes([]))
    # Expected: []

    # Example 5: Single-character usernames.
    print(find_all_palindromes(["A", "B"]))
    # Expected: ["A", "B"]