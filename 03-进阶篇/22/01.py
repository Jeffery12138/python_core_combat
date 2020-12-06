#! /usr/bin/env python3
# coding=utf-8

import asyncio
import aiohttp
import time


headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.149Safari/537.36',
    'Content-Type': 'text/html;charset = utf-8'
}


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'https://bk.tw.lvfukeji.com/wiki/Arts',
        'https://bk.tw.lvfukeji.com/wiki/History',
        'https://bk.tw.lvfukeji.com/wiki/Society',
        'https://bk.tw.lvfukeji.com/wiki/Biography',
        'https://bk.tw.lvfukeji.com/wiki/Mathematics',
        'https://bk.tw.lvfukeji.com/wiki/Technology',
        'https://bk.tw.lvfukeji.com/wiki/Geography',
        'https://bk.tw.lvfukeji.com/wiki/Science',
        'https://bk.tw.lvfukeji.com/wiki/Computer_science',
        'https://bk.tw.lvfukeji.com/wiki/Python_(programming_language)',
        'https://bk.tw.lvfukeji.com/wiki/Java_(programming_language)',
        'https://bk.tw.lvfukeji.com/wiki/PHP',
        'https://bk.tw.lvfukeji.com/wiki/Node.js',
        'https://bk.tw.lvfukeji.com/wiki/The_C_Programming_Language',
        'https://bk.tw.lvfukeji.com/wiki/Go_(programming_language)',
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {:.2f} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()