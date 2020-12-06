#! /usr/bin/env python3
# coding=utf-8

import time
from threading import Thread


def CountDown(n):
    while n > 0:
        n -= 1


def main():
    n = 100000000
    start_time = time.perf_counter()
    t1 = Thread(target=CountDown, args=[n // 2])
    t2 = Thread(target=CountDown, args=[n // 2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print('running time: {:.2f} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
