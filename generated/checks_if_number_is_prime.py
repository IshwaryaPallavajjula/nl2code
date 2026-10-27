def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, otherwise False.

    Args:
        n (int): The integer to test.

    Raises:
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False
    return True
