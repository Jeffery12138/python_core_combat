#! /usr/bin/env python3
# coding=utf-8

import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    start_time = time.perf_counter()
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')
    end_time = time.perf_counter()
    print('running time: {:.2f}'.format(end_time-start_time))


if __name__ == '__main__':
    asyncio.run(main())

