def is_palindrome(s):
    return s == s[::-1]


def all_substrings(s):
    string_length = len(s)
    for i in range(string_length):
        substring_length = string_length - i
        for j in range(i + 1):
            yield s[j:j + substring_length]

    yield ""


def longest_palindrome(s):
    return next(p for p in all_substrings(s) if is_palindrome(p))


if __name__ == "__main__":
    print("Enter a word or phrase to find its longest palindrome")
    while True:
        print(longest_palindrome(input("> ")))
