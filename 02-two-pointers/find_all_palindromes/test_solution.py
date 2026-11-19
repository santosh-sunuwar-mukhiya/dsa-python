import unittest

from solution import find_all_palindromes


class TestFindAllPalindromes(unittest.TestCase):

    def test_example_one(self):
        usernames = [
            "Tricer66",
            "TREXerT",
            "Veloc1COLEv",
            "stego95"
        ]

        expected = ["TREXerT", "Veloc1COLEv"]

        self.assertEqual(
            find_all_palindromes(usernames),
            expected
        )

    def test_example_two(self):
        usernames = ["nigersaurus111", "BRACHI33"]

        self.assertEqual(
            find_all_palindromes(usernames),
            []
        )

    def test_mixed_case_palindrome(self):
        usernames = ["Bob", "zAAaaZ"]

        self.assertEqual(
            find_all_palindromes(usernames),
            ["Bob", "zAAaaZ"]
        )

    def test_empty_array(self):
        self.assertEqual(
            find_all_palindromes([]),
            []
        )

    def test_single_character(self):
        self.assertEqual(
            find_all_palindromes(["A", "7"]),
            ["A", "7"]
        )

    def test_all_palindromes(self):
        usernames = ["madam", "racecar", "level"]

        self.assertEqual(
            find_all_palindromes(usernames),
            usernames
        )

    def test_no_palindromes(self):
        usernames = ["hello", "python", "world"]

        self.assertEqual(
            find_all_palindromes(usernames),
            []
        )


if __name__ == "__main__":
    unittest.main()