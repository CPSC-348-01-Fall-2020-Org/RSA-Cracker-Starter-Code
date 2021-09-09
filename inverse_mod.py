def inverse_mod(num, modulus):
    """Returns the inverse mod of the given number with respect to the given modulus."""
    gcd, x, _ = extended_euclidean_gcd(num, modulus)
    if gcd != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % modulus


def extended_euclidean_gcd(a, b):
    """Returns (gcd, x, y) such that a*x + b*y equals the greatest common denominator or a and b."""
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, y, x = extended_euclidean_gcd(b % a, a)
        return (gcd, x - (b // a) * y, y)
