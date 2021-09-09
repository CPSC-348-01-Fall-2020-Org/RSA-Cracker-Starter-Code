from test_rsa import test_rsa


def main():
    """
    Displays the results of the test cases using the following format.
    If the expected d value is unknown, displays "Expected: Unknown".
    If the key is too large for the brute-force algorithm, instead of displaying the time, displays "Could not crack the key using brute force.".

    ************************ Test Case 1 - 6 bits ************************

    Inputs:
            n: 33
            e: 7

    plaintext:
            Expected: 11
            Actual:   11
    ciphertext:
            Expected: 11
            Actual:   11
    d:
            Expected: 3
            Actual:   3

    Cracking time:                  0.0 seconds.
    Brute-force cracking time:      0.0 seconds.



    ************************ Test Case 2 - 6 bits ************************
                                    ...

                                    ...


    ************************ Test Case 10 - 89 bits ************************

    Inputs:
            n: 337280666197853981964619871
            e: 65537

    plaintext:
            Expected: 1010
            Actual:   1010
    ciphertext:
            Expected: 81243128398559957992827824
            Actual:   81243128398559957992827824
    d:
            Expected: Unknown
            Actual:   <your_answer_here>

    Cracking time:                  0.98 seconds.
    Could not crack the key using brute force.
    """
    return


if __name__ == "__main__":
    main()
