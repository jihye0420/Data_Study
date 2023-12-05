def multiply(num1, num2):
    """
    들어온 값을 제곱하는 함수입니다.

    >>> multiply(3, 5)
    15

    >>> multiply(6, 8)
    48
    """
    return num1 * num2

import doctest
doctest.testmod(verbose=True) # verbose 인수 제외