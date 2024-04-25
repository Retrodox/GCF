from prime_factorization import get_prime_factors

def find_gcf(num1, num2):
    factors1 = get_prime_factors(num1)
    factors2 = get_prime_factors(num2)
    
    # Count the frequency of each factor in both numbers
    from collections import Counter
    count1 = Counter(factors1)
    count2 = Counter(factors2)
    
    # Find minimum count for each common prime factor
    common_factors = set(factors1) & set(factors2)
    gcf = 1
    for factor in common_factors:
        gcf *= factor ** min(count1[factor], count2[factor])
    
    return gcf