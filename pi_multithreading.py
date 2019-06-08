import math # pi is 3.141592653589793
import time
import multiprocessing
import os
import sys
from pympler import asizeof
import threading
import concurrent.futures
import math

print(math.pi)
pi = 1.0


#        0     1      2    3
# PI/4 = 1/1 - 1/3 + 1/5 - 1/7 ...
#
def calculate_pi_v1(n):
    n = 2 * n + 1
    a = 0.0
    for i in range(1, n, 4):
        a += 1 / i
    for i in range(3, n, 4):
        a += -1 / i
    return a * 4.0


def calculate_pi_v5(n, array=None):
    a = 0.0
    plus = True
    for i in range(n):
        j = 1 if plus else -1
        plus = not plus
        c = j / (2 * i + 1)
        if array:
            array[i] = c
        a += c
    return a * 4.0

def calculate_pi_v6(args):
    # def calculate_pi_v6(n1, n2, array=None):
    # PI/4 = 1/1 - 1/3 + 1/5 - 1/7
    (n1, n2, array) = args
    a = 0.0
    plus = True
    for i in range(n1, n2):
        j = 1 if plus else -1
        plus = not plus
        c = j / (2 * i + 1)
        if array:
            array[i] = c
        a += c
    return a * 4.0


#        0     1      2    3
# PI/4 = 1/1 - 1/3 + 1/5 - 1/7 ...
#
def calculate_pi_v7(args):
    (n1, n2, array) = args
    even = False if n1 & 1 else True
    a = 0.0
    i1 = 2 * n1 + 1
    i2 = 2 * n2 + 1
    k = n1 if even else n1 + 1
    i0 = i1 if even else i1 + 2
    for i in range(i0, i2, 4):
        c = 1 / i
        if array:
            array[k] = c
            k += 2
        a += c
    k = n1 + 1 if even else n1
    i0 = i1 + 2 if even else i1
    for i in range(i0, i2, 4):
        c = -1 / i
        if array:
            array[k] = c
            k += 2
        a += c
    # print(n1, n2, array)
    return a * 4.0

# 100_000_000
# 100_000_000
# 3.1415926435801427 1.0009650441844542e-08 6.599581675000001 ( 1 2 )
# 3.141592643589326 1.0000467121074053e-08 13.978217202999998 ( 2 1 )
# 3.1415926435801427 1.0009650441844542e-08 49.543827829 ( 1 2 )
# 3.141592643589326 1.0000467121074053e-08 52.915389687 ( 2 1 )


def is_confirmed(args_data):
    for i, x in enumerate(args_data):
        if x != 1.0 / float(2 * i + 1) * [1, -1][i & 1]:
            print('****Failure', i, x, 1.0 / float(2 * i + 1) * [1, -1][i & 1])
            return False
    return True


def compare_functions(function_list, argument1, argument2):
    m = len(function_list)
    values = [0.0] * m
    errors = [0.0] * m
    times = [0.0] * m
    for i, f in enumerate(function_list):
        t = time.perf_counter()
        M = 4
        args = []
        n = argument1 // M
        for m in range(M):
            i0 = n * m
            i1 = i0 + n if m + 1 < M else argument1
            args.append((i0, i1, argument2))
            print(i0, i1)
        p = multiprocessing.Pool(processes=4)
        value = sum(list(p.imap(f, args)))
        # threads = {}
        # results = []
        # n = argument1 // M
        # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        #     for m in range(M):
        #         results.append(None)
        #         i0 = n * m
        #         i1 = i0 + n if m + 1 < M else argument1
        #         # threads[executor.submit(f, args=(i0, i1, argument2))] = None
        #         threads[executor.submit(f, args=(i0, i1, argument2))] = None
        #     value = 0.0
        #     for thread in concurrent.futures.as_completed(threads):
        #         v = thread.result()
        #         value += v
        #         # print(s)
        values[i] = value
        if argument2:
            is_confirmed(argument2)
        times[i] = time.perf_counter() - t
        errors[i] = abs(math.pi - values[i])
    rank_time = [sorted(times).index(t) + 1 for t in times]
    rank_errors = [sorted(errors).index(t) + 1 for t in errors]
    for i, f in enumerate(function_list):
        print(values[i], errors[i], times[i],
              '(', rank_time[i], rank_errors[i], ')')


f_list = [calculate_pi_v6, calculate_pi_v7]
n = 10
while n <= 100000000:
# while n <= 10:
    print(n)
    # data = [0.0] * n
    data = None
    compare_functions(f_list, n, data)
    print(data)
    n *= 10
exit(0)

def calculate_pi_v1_a(start, total):
    m = 2 * start + 1
    n = 2 * (total - 1) + 2
    a = 0.0
    for i in range(1, n, 4):
       a += 1 / i
    for i in range(3, n, 4):
       a -= 1 / i
    return a * 4.0


def calculate_pi_v2(n):
    data = [0.0] * n
    n = 2 * (n - 1) + 2
    k = 0
    for i in range(1, n, 4):
        data[k] = 1 / i
        k += 2
    k = 1
    for i in range(3, n, 4):
        data[k] = -1 / i
        k += 2
    b = 0.0
    return data
# def calculate_pi_v2(n):
#     data = [0.0] * n
#     for i in range(n):
#         data[i] = 1.0 / (float(2 * i + 1) * [1, -1][i & 1])
#     return data


def calculate_pi_v3(args):
    # PI/4 = 1/1 - 1/3 + 1/5 - 1/7
    (i0, i1, time0) = args
    t1 = time.time() - time0
    t1s = time.ctime()
    j0 = 2 * i0 + 1
    j1 = 2 * i1 + 2
    a = 0.0
    # k = i0
    # print(i0, i1, j0, j1)
    for i in range(j0, j1, 4):
        c = 1 / i
        a += c
        # d[k] = c
        # print(k, i, c)
        # k += 2
    # k = i0 + 1
    for i in range(j0 + 2, j1, 4):
        c = -1 / i
        a += c
        # d[k] = c
        # print(k, i, c)
        # k += 2
    t2 = time.time() - time0
    t2s = time.ctime()
    s = '# %s %d %.2f %.2f %s %s %d %d' % (
        format(os.getpid()), threading.get_ident(), t1, t2, t1s, t2s, i0, i1)
    return a * 4.0, s


def calculate_pi_v4(args):
    (args_data, data_first, data_last) = args
    for i in range(data_first, data_last + 1):
        args_data[i] = 1.0 / (float(2 * i + 1) * [1, -1][i & 1])


if __name__ == '__main__':  # Testing ... #####################################
    def main():

        # N = 100_000_000
        N = 100_000_000
        start = time.time()
        v1 = calculate_pi_v1(N)
        total_time = time.time() - start
        d1 = abs(math.pi - v1)
        print(v1, d1, total_time)

        start = time.time()
        d = calculate_pi_v2(N)
        total_time = time.time() - start
        d1 = abs(math.pi - v1)
        v1 = sum(d) * 4.0
        d1 = abs(math.pi - v1)
        print(v1, d1, total_time)

        start = time.time()
        print(time.ctime())
        t0 = time.time()
        # d = [0.0] * N
        M = 4
        threads = {}
        results = []
        n = N // M

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(M):
                results.append(None)
                i0 = n * i
                j = i + 1
                i1 = i0 + n - 1 if i + 1 < M else N - 1
                # threads[executor.submit(calculate_pi_v3, args=(d, i0, i1, start))] = None
                threads[executor.submit(calculate_pi_v3, args=(i0, i1, t0))] = None
            v2 = 0.0
            for t in concurrent.futures.as_completed(threads):
                v1, s = t.result()
                v2 += v1
                print(s)
        d2 = abs(math.pi - v2)
        print(v2, d2)

        total_time = time.time() - start
        print(time.ctime())
        print('Total %.2f seconds' % total_time )
        if total_time  > 0.0:
            print('%.2f MGOPops' % (N/total_time /1_000_000.))

    main()
