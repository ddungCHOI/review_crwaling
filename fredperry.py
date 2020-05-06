import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.fredperrykorea.com/main/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
req = requests.get(url, headers = headers)
soup = BeautifulSoup(req.content, 'html.parser')

tags = soup.select('div.sub.category > ul.list > li')

cate_dict = {}
val_dict = {}

for key in tags:
    title = key.select('a.title')[0].text 
    cate_dict[title] = {}

    for val in key.select('li > ul > li > a'):
        val_dict[val.text] = re.findall("\d+", val['href'])
        cate_dict[title] = val_dict
    val_dict = {}

print(cate_dict)