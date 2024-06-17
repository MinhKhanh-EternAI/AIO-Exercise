import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def approx_sin(x, n):
    result = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    print(f"approx_sin = {result}")
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i)) / factorial(2*i)
        result += term
    print(f"approx_cos = {result}")
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    print(f"approx_sinh = {result}")
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = (x**(2*i)) / factorial(2*i)
        result += term
    print(f"approx_cosh = {result}")
    return result


if __name__ == "__main__":
    approx_sin(x=3.14, n=10)
    approx_cos(x=3.14, n=10)
    approx_sinh(x=3.14, n=10)
    approx_cosh(x=3.14, n=10)
