from palindromes import is_palindrome, all_substrings, longest_palindrome
import unittest

palindrome_strings = {"", "A", "AA", "ABA", "ABBA", "tattarrattat", "deleveled", "redivider"}
random_strings = {"ABC", "palindrome", "something", "wordswordswords"}


class PalindromesTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        for s in palindrome_strings:
            self.assertTrue(is_palindrome(s), "{} should be a palindrome".format(s))

        for s in random_strings:
            self.assertFalse(is_palindrome(s), "{} should not be a palindrome".format(s))

    def test_all_substrings(self):
        self.assertEqual(list(all_substrings("")), [""])
        self.assertEqual(list(all_substrings("A")), ["A", ""], "All substrings of A")
        self.assertEqual(list(all_substrings("ABC")), ["ABC", "AB", "BC", "A", "B", "C", ""], "All substrings of ABC")

    def test_longest_palindrome(self):
        for s in palindrome_strings:
            self.assertEqual(longest_palindrome(s), s, "Longest palindrome in {} should be itself".format(s))

        self.assertEqual(longest_palindrome("ABC"), "A", "Longest palindrome in ABC should be A")
        self.assertEqual(longest_palindrome("AABBBCC"), "BBB", "Longest palindrome in AABBBCC should be BBB")


if __name__ == "__main__":
    unittest.main()
