def isPrime(n, k, a):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    for i in range(k):
        if pow(a[i], n - 1, n) != 1:
            return False
    return True
