# Python DSA — Data Structures & Algorithms

A structured journey of learning and practicing **Data Structures and Algorithms using Python**, focused on problem-solving, understanding core concepts, and preparing for software engineering interviews.

This repository contains my implementations, explanations, approaches, and complexity analysis as I progress through different DSA topics.

## 🎯 Objectives

- Build strong problem-solving skills.
- Understand fundamental data structures and algorithms.
- Learn to analyze time and space complexity (Big O).
- Recognize common coding interview patterns.
- Solve problems independently rather than memorizing solutions.
- Prepare for technical interviews at product-based companies.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Practice Platform:** LeetCode
- **Learning Roadmap:** NeetCode 150
- **Version Control:** Git & GitHub

## 📚 Topics & Progress

| # | Topic | Progress |
|---|---|---|
| 01 | Big O, Arrays & Hashing | 1 / 20 |
| 02 | Two Pointers | 0 / 10 |
| 03 | Sliding Window | 0 / 5 |
| 04 | Stack & Queue | 0 / 10 |
| 05 | Linked Lists | 0 / 5 |
| 06 | Binary Search & Sorting | 0 / 10 |
| 07 | Trees & Binary Search Trees | 0 / 20 |
| 08 | Heaps & Priority Queues | 0 / 10 |
| 09 | Backtracking & Tries | 0 / 15 |
| 10 | Graphs (BFS & DFS) | 0 / 15 |
| 11 | Greedy & Dynamic Programming | 0 / 20 |
| 12 | Advanced Graphs & Bit Manipulation | 0 / 10 |
| | **Total Target** | **0 / 150** |

*Progress will be updated as I solve and understand each problem.*

## 📁 Repository Structure

```text
dsa-python/
│
├── 01-arrays-hashing/
├── 02-two-pointers/
├── 03-sliding-window/
├── 04-stack-queue/
├── 05-linked-list/
├── 06-binary-search/
├── 07-trees/
├── 08-heaps/
├── 09-backtracking/
├── 10-graphs/
├── 11-greedy-dp/
├── 12-advanced/
│
└── README.md
```

Each topic folder contains individual Python solutions organized by problem.

## 🧠 Problem-Solving Approach

For every problem, I aim to:

1. Understand the problem and its constraints.
2. Think of a brute-force solution.
3. Identify opportunities for optimization.
4. Implement the solution in Python.
5. Analyze time and space complexity.
6. Test edge cases.
7. Document the approach and lessons learned.

Example:

```python
"""
Problem: Two Sum
Pattern: Hash Map
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a hash map to find the complement
of the current number in constant time.
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
```

## 📈 Learning Resources

- [NeetCode 150](https://neetcode.io/roadmap)
- [LeetCode](https://leetcode.com/)
- [Python Official Documentation](https://docs.python.org/3/tutorial/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

## 💻 How to Run the Solutions

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/dsa-python.git
```

Navigate into the project:

```bash
cd dsa-python
```

Run an individual solution:

```bash
python3 01-arrays-hashing/two_sum.py
```

## 📌 Progress & Consistency

My focus is not simply solving 150 problems. I want to understand the underlying patterns, improve my problem-solving ability, and become confident enough to implement solutions independently.

I will regularly update this repository with new solutions, improvements, and concepts learned.

---

**Learning by solving. Improving through consistency. Building strong engineering fundamentals.**
