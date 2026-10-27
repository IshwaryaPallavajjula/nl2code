def count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given string.
    Both uppercase and lowercase vowels are counted.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)
