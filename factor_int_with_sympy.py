from sympy.ntheory import factorint
import sys
sys.path.append("./lib")


def factor_int_with_sympy(num):
    """
    Returns a tuple with the two prime factors of the given number.
    This uses sympy's factorint function, documented here: https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.factorint
    """
    factors_of_n = factorint(num)

    # since n is the product of two primes, we know its only factors are those two primes
    # if this is not the case, n is invalid (i.e., not the product of two primes)
    factors_are_valid = len(factors_of_n) == 2 and all(
        multiplicity == 1 for multiplicity in factors_of_n.values())
    if (not factors_are_valid):
        raise Exception(f"{num} is not the product of two primes.")

    factors_list = list(factors_of_n)
    p = factors_list[0]
    q = factors_list[1]
    return p, q
