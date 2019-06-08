import math
import time
import platform
import sys
from itertools import cycle, starmap
from operator import truediv

# Functions with '*leibniz*' name must be Pythonic stanza (one-liner)
# but the statement can span multiple lines if over "Maximum Line Length"
# [79 characters in PEP 8 -- Style Guide for Python Code]


def madhava_leibniz_starmap(k, n):
    return starmap(truediv, zip(cycle([1, -1] if k & 1 else [1, -1]),
                                range(2*k+1, 2*n+2, 2)))


def madhava_leibniz(k, n):
    return [s / d for s, d in zip(cycle([1, -1] if k & 1 else [1, -1]),
                                  range(2*k+1, 2*n+2, 2))]


def leibniz(k, n):
    return [[1.0, -1.0][i % 2] / (2 * i + 1) for i in range(k, n+1)]


# Functions without '*leibniz*' but with 'madhava' pattern in the name are
# optimized for speed any way you like. Can be multiple statements.


def madhava(k, n):
    series = [0.0] * (n - k + 1)
    first_divisor = 2 * k + 1
    last_divisor_plus_1 = 2 * n + 2
    i = 0
    if k & 1:
        for divisor in range(first_divisor, last_divisor_plus_1, 4):
            series[i] = -1 / divisor
            i += 2
        i = 1
        for divisor in range(first_divisor + 2, last_divisor_plus_1, 4):
            series[i] = 1 / divisor
            i += 2
    else:
        for divisor in range(first_divisor, last_divisor_plus_1, 4):
            series[i] = 1 / divisor
            i += 2
        i = 1
        for divisor in range(first_divisor + 2, last_divisor_plus_1, 4):
            series[i] = -1 / divisor
            i += 2
    return series


if __name__ == '__main__':  # Testing ... #####################################
    def print_platform_info():
        print(platform.node())
        (mac_ver, _, _) = platform.mac_ver()
        print(platform.python_version_tuple())
        if mac_ver is not None and mac_ver != "":
            print("macOS version", mac_ver)
        print(platform.platform())
        print("Python", platform.python_build(), platform.python_compiler())
        print("Executing in", "64bit" if sys.maxsize > 2 ** 32 else "32bit")

    def report(f, m, n):  # Test a function: time and returned values
        t = time.time()
        series = []
        for i in range(m):
            series += f(i * n, (i + 1) * n - 1)
        p = sum(series) * 4.0
        t = time.time() - t
        print('{:6.3f}{:19.15f} {} {}'.format(t, p, math.pi - p, f.__name__))
        if len(series) != n * m:
            print('Error! length {}, requested {}'.format(len(series), n * m))
            exit(1)
        sign = [1.0, -1.0]
        for i, a in enumerate(series):
            e = sign[i % 2] / (2 * i + 1)
            if a != e:
                print(
                    'Error! @ {} actual value {}, expected {}'.format(i, a, e))
                exit(1)

    def main():
        m = 4
        n = 25_000_000
        s = 'chunks * elements = m * n = {:,} * {:,} = {:,}'.format(m, n, m*n)
        print('\n', s, '\n')
        print('Time Pi%18.15f Error of calculation   function' % math.pi)
        for f in [leibniz, madhava, madhava_leibniz, madhava_leibniz_starmap]:
            report(f, m, n)

    main()
