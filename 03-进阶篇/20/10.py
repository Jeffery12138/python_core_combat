#! /usr/bin/env python3
# coding=utf-8

import asyncio
import aiohttp
import time
import requests

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.149Safari/537.36',
    'Content-Type': 'text/html;charset = utf-8'
}


async def fetch_content(url):
    async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector()) as session:
        async with session.get(url) as response:
            return await response.text()


def fetch_img(url):
    response = requests.get(url, headers=headers)
    return response.content


async def main():
    start_time = time.perf_counter()

    url = 'https://movie.douban.com/cinema/later/beijing/'
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')

    movie_names, urls_to_fetch, movie_dates = [], [], []
    
    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item mod"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

        # img_url = img_tag['src']
        # res = fetch_img(img_url)
        # img_name = img_url.split('/')[-1][-4:]
        # with open('images/{}{}'.format(movie_name, img_name), 'wb') as f:
        #     f.write(res)

    end_time = time.perf_counter()
    print('crawling time: {:.2f} s'.format(end_time-start_time))

if __name__ == '__main__':
    asyncio.run(main())
