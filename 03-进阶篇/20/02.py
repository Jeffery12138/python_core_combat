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
    for url in urls:
        await crawl_page(url)
    end_time = time.perf_counter()
    print('running time: {:.2f}'.format(end_time - start_time))
    print(crawl_page(''))


if __name__ == '__main__':
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
    print(crawl_page(''))
