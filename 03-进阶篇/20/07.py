#! /usr/bin/env python3
# coding=utf-8

import asyncio
import time


async def worker_1():
    await asyncio.sleep(1)
    return 1


async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0


async def worker_3():
    await asyncio.sleep(3)
    return 3


async def main():
    start_time = time.perf_counter()
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()
    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)
    end_time = time.perf_counter()
    print('running time: {:.2f}'.format(end_time-start_time))


if __name__ == '__main__':
    asyncio.run(main())
