def reverse_words(sentence: str) -> str:
    """
    Return a new string with the order of words in the input sentence reversed.
    Words are defined as sequences of characters separated by whitespace.
    Multiple consecutive whitespace characters are treated as a single separator.
    An empty input returns an empty string.
    """
    if not sentence:
        return ""
    words = sentence.split()
    return " ".join(reversed(words))
