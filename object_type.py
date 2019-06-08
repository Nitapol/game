# numberList = [1, 2]
# strList = ['one', 'two', 'three']
#
# # No iterables are passed
# result = zip()
# print(result)
#
# # Converting itertor to list
# resultList = list(result)
# print(resultList)
#
# # Two iterables are passed
# result = zip(numberList, strList)
# print(result)
#
# # Converting itertor to set
# resultSet = set(result)
# print(resultSet)
#
# exit(0)
#
# import pathos
# #import multiprocess
# #import multiprocessing
# import time
# from pympler import asizeof
# import sys
# import os
#
#
# def f(args):
#     (x, graph) = args
#     t = time.ctime()
#     print('pid %s factorial of %d: start@%s' % (format(os.getpid()), x, t))
#     time.sleep(4)
#     return x
#
#
# def main():
#     t0 = time.time()
#     params = []
#
#     var = (4, 8, 12, 20, 16)
#     p = pathos.multiprocessing.ProcessPool(nodes=4)
#     #  p = multiprocessing.Pool(processes=4)
#     N = 200
#     import networkx as nx
#     G = nx.complete_graph(N, nx.DiGraph())
#
#     import random
#     for (start, end) in G.edges:
#         G.edges[start, end]['weight'] = random.random()
#
#     print('Size of G by sys', sys.getsizeof(G), 'asizeof', asizeof.asizeof(G))
#     print('G created in %.2f' %  (time.time() - t0))
#
#     for i in var:
#         params.append((i, G))
#     res = list(p.map(f, params))
#
# if __name__ == '__main__':
#     main()

import pathos
# import multiprocessing
import os
import time
import sys
from pympler import asizeof
import networkx as nx
import random


def factorial(args):
    (x, t, graph) = args
    s0 = '# pid %s x %2d' % (format(os.getpid()), x)
    s1 = 'started @ %.2f' % (time.time() - t)
    print(s0, s1)
    f = 1
    while x > 1:
        f *= x
        x -= 1
        time.sleep(0.5)
    s2 = 'ended   @ %.2f' % (time.time() - t)
    print(s0, s2, f)
    return s0, s1, s2, f


if __name__ == '__main__':
    t0 = time.time()
    N = 400
    G = nx.complete_graph(N, nx.DiGraph())
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = random.random()
    print('Size of G by sys', sys.getsizeof(G), 'asizeof', asizeof.asizeof(G))
    print('G created in %.2f' %  (time.time() - t0))
    t0 = time.time()
    p = pathos.multiprocessing.ProcessPool(nodes=4)
    # p = multiprocessing.Pool(processes=4)
    outputs = list(p.imap(factorial, [(i, t0, G) for i in (4, 8, 12, 20, 16)]))
    print('output:')
    for output in outputs:
        print(output)

# import pygame
# from pygame.locals import *
# import keyboard;
#
# def draw():
#     pygame.init();
#     x=1280
#     y=720
#     screen=pygame.display.set_mode((x, y))
#     font = pygame.font.Font('freesansbold.ttf', 24)
#     black=(0, 0, 0)
#     white=(255, 255, 255)
#     text = font.render('0', True, black, white)
#     textRect = text.get_rect()
#     x=x/2; y=y/2;
#     textRect.center=(x, y)
#     screen.fill((white))
#     screen.blit(text, textRect)
#
#
#     while True:
#         if keyboard.is_pressed('w'):
#             textRect = text.get_rect()
#             y = y - 5;
#             textRect.center = (x, y)
#             # screen.fill((white))
#             screen.blit(text, textRect)
#
#         if keyboard.is_pressed('a'):
#             textRect = text.get_rect()
#             x = x - 5;
#             textRect.center = (x, y)
#             # screen.fill((white))
#             screen.blit(text, textRect)
#         if keyboard.is_pressed('d'):
#             textRect = text.get_rect()
#             x = x + 5;
#             textRect.center = (x, y)
#             # screen.fill((white))
#             screen.blit(text, textRect)
#         if keyboard.is_pressed('s'):
#             textRect = text.get_rect()
#             y = y + 5;
#             textRect.center = (x, y)
#             # screen.fill((white))
#             screen.blit(text, textRect)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit();
#                 quit();
#             pygame.display.update()
#
# if __name__=="__main__":
#     draw()
#
# exit(0)
#
# a = {'red': 'blue', 'yellow': 'green', 'blue': 'blue1'}
# b = {'red': 'black', 'yellow': 'white'}
#
# a = {**a, **b}
# # for i, j in b.items():
# #     if i in a:
# #         a[i] = j
# print(a)
#
# exit(0)
#
# import time
#
#
# def question_by_akrapovich(data):
#     for index in range(len(data)):
#         if (index + 1) % 3 == 0:
#             data[index] = data[index] * 2
#     return data
#
#
# def answer_by_Tom_Karzes_and_Prune(data):
#     for index in range(2, len(data), 3):
#         data[index] *= 2
#     return data
#
#
# def answer_by_Blorgbeard(data):
#     data[2::3] = [x*2 for x in data[2::3]]
#     return data
#
#
# def answer_1_by_Alain_T(data):
#     from itertools import cycle
#     return [n * m for n, m in zip(data, cycle([1, 1, 2]))]
#
#
# def answer_2_by_Alain_T(data):
#     return [ n*max(1,i%3) for i,n in enumerate(data) ]
#
#
# def answer_by_Manuel_Montoya(data):
#     for index in range(2, len(data), 3):
#         data[index] = data[index]*2
#     return  data
#
# def answer_by_Alex(data):
#     return [ n*2 if i %3 == 2 else n for i, n in enumerate(data)]
#
#
# def answer_2_by_Alex(data):
#     from itertools import islice
#     data[2::3] = (x * 2 for x in islice(data, 2, None, 3))
#     return  data
#
#
# def test(f):
#     n = 10_000_000
#     data = [i + 1 for i in range(n)]
#     start_time = time.perf_counter()
#     data = f(data)
#     run_time = time.perf_counter() - start_time
#     if n != len(data):
#         print('error in list length', n, len(data))
#         exit(1)
#     for i in range(n):
#         j = i + 1
#         m = j * 2 if j % 3 == 0 else j
#         if data[i] != m:
#             print('error in data', i, m, data[i])
#             exit(1)
#     print('%.3f %s' % (run_time, f.__name__))
#
# test(answer_2_by_Alex)
# test(answer_by_Alex)
#
# print('Calculation time in seconds and results validation test.')
# for f in [question_by_akrapovich, answer_by_Tom_Karzes_and_Prune,
#           answer_by_Manuel_Montoya, answer_by_Blorgbeard,
#           answer_1_by_Alain_T, answer_2_by_Alain_T, answer_by_Alex]:
#     test(f)

# import random
# variable = 1
# variable = None
# for i in range(10):
#     variable = random.randint(1, 3)
#     if variable <= 0:
#         variable = 'Zero or less'
#     elif variable == 1:
#         variable = 1.0
#     elif variable == 2:
#         variable = [2]
#     elif variable == 3:
#         variable = {'three': 3}
#     else:
#         variable = (4, '4 or more')
#     print(i, type(variable), variable)
# # Extra blank lines to show variable type
# #
# #
# #
# del variable
