
# Time Pi 3.141592653589793 Error of calculation   Comment
#  2.143  3.141592553589792 1.0000000161269895e-07 List comprehension
#  1.980  3.141592553589792 1.0000000161269895e-07 Four 'for' loop [even, odd] [(inline, no function calls)
#  1.162  3.141592553589792 1.0000000161269895e-07 List as argument in function call (same for loop)
#  0.592  3.141592553586459 1.0000333405812967e-07 not series, just a summation
#  0.821  3.141592654347848 -7.580545080543288e-10 Dummy series 1: function assigns all list elements to math.pi
#  0.485  3.141592654347848 -7.580545080543288e-10 Dummy series 2: function assign all list elements to pi (local)
#  0.129  3.141592654347848 -7.580545080543288e-10 Dummy series 3: List comprehension to local pi
#  0.141  3.141592654347848 -7.580545080543288e-10 Dummy series 4: List comprehension to math.pi
# Time Pi 3.141592653589793 Error of calculation   Comment
#  1.096  3.141592553589792 1.0000000161269895e-07 madhava
#  2.240  3.141592553589792 1.0000000161269895e-07 sangamagrama
#  2.090  3.141592553589792 1.0000000161269895e-07 List comprehension
#  2.050  3.141592553589792 1.0000000161269895e-07 Two for loop (inline, no function calls)
#  1.118  3.141592553589792 1.0000000161269895e-07 List as argument in function call (same for loop)
#  0.567  3.141592553586459 1.0000333405812967e-07 not series, just a summation
#  0.800  3.141592654347848 -7.580545080543288e-10 Dummy series 1: function assigns all list elements to math.pi
#  0.476  3.141592654347848 -7.580545080543288e-10 Dummy series 2: function assign all list elements to pi (local)
#  0.071  3.141592654347848 -7.580545080543288e-10 Dummy series 3: List comprehension to local pi
#  0.081  3.141592654347848 -7.580545080543288e-10 Dummy series 4: List comprehension to math.pi


# def dummy1(n, series):
#     for i in range(n):
#         series[i] = math.pi
#
#
# def dummy2(n, series):
#     pi = math.pi
#     for i in range(n):
#         series[i] = pi
#
#
# series1 = [[1.0, -1.0][i % 2] / (2 * i + 1) for i in range(n)]
# pi = sum(series1) * 4.0
# report('List comprehension')
#
# series2 = [0.0] * n
# n2plus1 = 2 * n + 1
# j = 0
# for i in range(1, n2plus1, 4):
#     series2[j] = 1 / i
#     j += 2
# j = 1
# for i in range(3, n2plus1, 4):
#     series2[j] = -1 / i
#     j += 2
# pi = sum(series2) * 4.0
# report('Two for loop (inline, no function calls)')
#
# series3 = [0.0] * n
# Madhava_of_Sangamagrama(n, series3)
# pi = sum(series3) * 4.0
# report('List as argument in function call (same for loop)')
#
#
# pi = Gottfried_Leibniz(n) * 4.0
# report('not series, just a summation')
#
# d1 = [0.0] * n
# dummy1(n, d1)
# pi = sum(d1) / n
# report('Dummy series 1: function assigns all list elements to math.pi')
#
# d2 = [0.0] * n
# dummy2(n, d2)
# pi = sum(d2) / n
# report('Dummy series 2: function assign all list elements to pi (local)')
#
# pi = math.pi
# d3 = [pi] * n
# pi = sum(d3) / n
# report('Dummy series 3: List comprehension to local pi')
#
# d4 = [math.pi] * n
# pi = sum(d4) / n
# report('Dummy series 4: List comprehension to math.pi')
# exit(0)
#
# #
# # Time Pi 3.141592653589793 Error (1_000_000_000)
# # 544.103   3.14159265258805 1.0017426887998226e-09 leibniz_series: List comprehension
#
# from math import pi
# # https://stackoverflow.com/questions/19550135/pi-calculation-in-python
# def leibniz():
#     from itertools import count
#     s, x = 1.0, 0.0
#     for i in count(1, 2):
#         x += 4.0*s/i
#         s = -s
#         yield x
#
# def avg(seq):
#     a = next(seq)
#     while True:
#         b = next(seq)
#         yield (a + b) / 2.0
#         a = b
#
# base = leibniz()
# d1 = avg(base)
# d2 = avg(d1)
# d3 = avg(d2)
# d4 = avg(d3)
# d5 = avg(d4)
#
# t = time.time()
# for i in range(2_000_000):
#     x = next(base)
# print("{:.6f} {:8.4%}".format(x, (x - pi)/pi))
# t = time.time() - t
# print('Calculation', t, 'seconds, PI value', x, 'PI error', math.pi - x)
# print(math.pi)
# print(x)
#
# exit(0)
#
# def calculate_pi_v2(n):
#     n = 2 * n + 1
#     a = 0.0
#     for i in range(1, n, 4):
#         a += 1 / i - 1 / (i + 2)
#     return a * 4.0
# # Time of calculation  62.595181941986084 seconds, PI 3.1415926445762157 error 9.013577439986875e-09
#
# t = time.time()
# # v = calculate_pi_v2(1000_000_000)
# for i in range(10_000_000):
#     v = next(d3)
#     # print("{:.6f} {:8.4%}".format(x, (x - pi)/pi))
# t = time.time() - t
# print('Calculation', t, 'seconds, PI value', v, 'PI error', math.pi - v)
