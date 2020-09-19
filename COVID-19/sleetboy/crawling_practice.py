"""
크롤러 만들기
1. input JSON 읽기 -> URL, 파일명 // 완료
2. 제목, 본문 크롤링
3. 크롤링 결과(text) 저장 // 완료
This is dev branch!
"""
# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib.request


def read_article_data(path):
    """ 뉴스 기사의 정보가 있는 [path]파일을 읽음 """
    with open(path) as fin:
        return json.load(fin).get('news')


def crawler(url):
    """ 크롤링 해서 결과 return """
    hdr = {"User-Agent": "Chrome/66.0.3359.181"}
    req = urllib.request.Request(url, headers=hdr)
    html = urlopen(req)
    bsObj = BeautifulSoup(html, "lxml")
    target_text = bsObj.text
    return target_text


def save_article_data(path, text):
    """ [text]의 내용을 [path]에 저장 """
    with open(path, 'w', encoding="utf-8") as fout:
        fout.writelines(text)


def main():
    path_in_json = '../news/news.json'
    path_out_dir = 'scrap_files'

    # read input data
    news = read_article_data(path_in_json)

    # crawling
    for article_info in tqdm(news, total=len(news)):
        text = crawler(article_info.get('url'))
        file_name = article_info.get('filename')

        path_out = os.path.join(path_out_dir, file_name)
        # path_out = path_out_dir + '/' + file_name
        # path_out = f'{path_out_dir}/{file_name}'

        save_article_data(path_out, text)
        # save_article_data(path_out, crawler(article_info.get('url')))


if __name__ == '__main__':
    main()
