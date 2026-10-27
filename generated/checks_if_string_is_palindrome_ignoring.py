def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome, ignoring case and punctuation.
    An empty string is considered a palindrome.
    Raises TypeError if the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]
