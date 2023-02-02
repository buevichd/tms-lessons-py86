def is_palindrome(s: str) -> bool:
    return s == ''.join(reversed(s))


print(is_palindrome('abba'))  # True
print(is_palindrome('abcd'))  # False
