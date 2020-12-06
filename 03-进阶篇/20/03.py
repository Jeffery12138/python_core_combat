#! /usr/bin/env python3
# coding=utf-8

import asyncio
import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
    end_time = time.perf_counter()
    print('running time: {:.2f}'.format(end_time - start_time))


if __name__ == '__main__':
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

