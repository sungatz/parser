import requests
import json
from bs4 import BeautifulSoup
# url = 'https://www.sulpak.kz/Stocks/Action/7698/novogodnee_predlozhenie_ot_razer'

# headers = {
#     "Accept": "*/*",
#     'user-agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
# }

# req = requests.get(url)
# src = req.text 
# # print (src)

with open('index.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')


all_categories = {}
all_headphones = soup.find_all(class_='product__item-narrow')
for item in all_headphones:
    item_text = item.text
    item_href = item.get("href")
    all_categories[item_text] = item_href

with open('all_categories.json', 'w', encoding='utf-8') as file:
    json.dump(all_categories, file, indent=4, ensure_ascii=False)