def isPrime(n, k, a):
    if n != 2 and n % 2 == 0:
        return False
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    r, s = 0, n - 1
    for i in range(k):
        x = pow(a[i], s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True
