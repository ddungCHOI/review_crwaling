import re
import requests
import json
from bs4 import BeautifulSoup

url = 'https://kr.louisvuitton.com/kor-kr/homepage'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
req = requests.get(url, headers = headers)
bs_obj = BeautifulSoup(req.content, 'html.parser')

#Category
product_dict = {}
products_dict = {}
category_dict = {}
meta={}

#Category
categories = bs_obj.select('ul.lv-header-main-nav.lv-list > li')
for cate1 in categories:
    cate1_name = cate1.select_one('span').get_text().strip()
    category_dict[cate1_name] = dict()

    categories2 = cate1.select('ul.lv-list.lv-header-main-nav-child > li')
    for cate2 in categories2:
        cate2_name = cate2.select_one('span').get_text().strip()
        category_dict[cate1_name][cate2_name] = dict()

        categories3 = cate2.select('ul.lv-list > li')
        for cate3 in  categories3:
            cate3_name = cate3.select_one('span').get_text().strip()
            cate3_code = cate3.select_one('a')['href']
            category_dict[cate1_name][cate2_name][cate3_name] = cate3_code

print(category_dict)