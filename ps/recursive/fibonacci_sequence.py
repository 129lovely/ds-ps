def recursive(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def iterative(n):
    if n <= 1:
        return n

    n1 = 1
    n2 = 0
    total = 0

    for _ in range(n - 1):
        total = n1 + n2
        n2 = n1
        n1 = total

    return total