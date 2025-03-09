# Convert a string into a pallindrome making least possible change.


def make_palindrome(s):
    s = list(s)  # Convert string to list (as strings are immutable in Python)
    left, right = 0, len(s) - 1
    changes = 0

    while left < right:
        if s[left] != s[right]:
            s[right] = s[left]  # Modify the right character to match the left
            changes += 1
        left += 1
        right -= 1

    return "".join(s), changes


# Example Usage
s = "abca"
result, changes = make_palindrome(s)
print(f"Modified Palindrome: {result}, Changes: {changes}")
