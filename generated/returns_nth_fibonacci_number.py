def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using 0-indexing:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
