#! /usr/bin/env python3
# coding=utf-8

import concurrent.futures
import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {:.2f} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()