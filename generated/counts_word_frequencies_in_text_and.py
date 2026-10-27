def count_word_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each word in the given text.

    Args:
        text: The input string to analyze.

    Returns:
        A dictionary mapping words to their occurrence counts.
        Words are compared case‑insensitively and punctuation is ignored.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    import re
    from collections import Counter

    # Find words: sequences of alphanumeric characters and underscores
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))
