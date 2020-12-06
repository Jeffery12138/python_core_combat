#! /usr/bin/env python3
# coding=utf-8


import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.149Safari/537.36',
    'Content-Type': 'text/html;charset = utf-8'
}


def main():
    start_time = time.perf_counter()
    url = 'https://movie.douban.com/cinema/later/beijing'

    init_page = requests.get(url, headers=headers).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item mod"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=headers).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

    end_time = time.perf_counter()
    print('crawling time: {:.2f} s'.format(end_time-start_time))


if __name__ == '__main__':
    main()


