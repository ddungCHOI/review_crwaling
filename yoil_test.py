import re
import requests
import json
from bs4 import BeautifulSoup

url = 'https://kr.louisvuitton.com/kor-kr/products/plaque-porte-adresse-horizon-nvprod1000230v'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
req = requests.get(url, headers = headers)
bs_obj = BeautifulSoup(req.content, 'html.parser')

#Category
product_dict = {}
products_dict = {}
category_dict = {}
meta={}

#Category
categories = bs_obj.select('#read-more > div > ul > li').get_text().strip()

for cate1 in categories:
#    cate1_name = cate1.select_one('span.lv-product-card__name').get_text().strip()
 #   category_dict[cate1_name] = dict()
#if "소재" in bs_obj.select_one('#read-more li').get_text().strip():
product_fabric = cate1.select_one('li').get_text()
print(categories)

