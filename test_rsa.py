from rsa_encryption import rsa_encrypt, rsa_decrypt
from rsa_cracker import crack_rsa, crack_rsa_brute_force


class RsaTestResult:
    """
    Members:

    d (int): The private exponent obtained by cracking RSA.
    ciphertext (int): The ciphertext obtained by encrypting the given plaintext with the given public key {e, n}.
    plaintext (int): The plaintext obtained by decrypting the ciphertext with the cracked d value.
    fast_time (float): The time in seconds taken by the fast cracking algorithm.
    brute_force_time (float): The time in seconds taken by the brute-force cracking algorithm.  (This will be None if brute force was not used.)
    """

    def __init__(self, d, plaintext, ciphertext, fast_time, brute_force_time):
        self.d = d
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.fast_time = fast_time
        self.brute_force_time = brute_force_time


def test_rsa(key_size, n, e, plaintext):
    """
    Tests RSA encryption and cracking with the given values.
    Returns a fully populated RsaTestResult object (except RsaTestResult.brute_force_time, which will be None for any keys larger than 55 bits).
    """
    return RsaTestResult(0, 0, 0, 0, 0)
