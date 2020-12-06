#! /usr/bin/env python3
# coding=utf-8

import time


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    start_time = time.perf_counter()
    for url in urls:
        crawl_page(url)
    end_time = time.perf_counter()
    print('running time: {:.2f} s'.format(end_time - start_time))


if __name__ == '__main__':
    main(['url_1', 'url_2', 'url_3', 'url_4'])
