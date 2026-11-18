"""
Problem: Get Age Range
Topic: Arrays
Difficulty: Beginner

Description:
Given an array of dinosaur ages, calculate the age range.

Age Range = Maximum Age - Minimum Age

Time Complexity: O(n)
Space Complexity: O(1)
"""

def get_age_ranges(ages):
    # Step 1: Initialize maximum and minimum with the first element.
    max_age = ages[0]
    min_age = ages[0]

    # Step 2: Find the maximum and minimum ages.
    for age in ages:
        if age > max_age:
            max_age = age
        
        if age < min_age:
            min_age = age
    
    # Step 3: Calculate and return the age range.
    return max_age - min_age


if __name__ == "__main__":
    print(get_age_ranges([8, 51, 3, 64, 1, 75, 9, 100]))  # Expected: 99
    print(get_age_ranges([8, 2, 5, 12, 3]))                # Expected: 10
    print(get_age_ranges([5, 5]))                         # Expected: 0
    print(get_age_ranges([5]))                            # Expected: 0
