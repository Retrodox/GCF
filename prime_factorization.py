def get_prime_factors(unfactored):
    i = 2
    factors = []
    while i * i <= unfactored:
        if unfactored % i:
            i += 1
        else:
            unfactored //= i
            factors.append(i)
    if unfactored > 1:
        factors.append(unfactored)
    return factors