#! /usr/bin/env python3
# coding=utf-8

import time


def CountDown(n):
    while n > 0:
        n -= 1


def main():
    n = 100000000
    start_time = time.perf_counter()
    CountDown(n)
    end_time = time.perf_counter()
    print('running time: {:.2f} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
