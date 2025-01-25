from bs4 import BeautifulSoup
with open('sigmaparser/skidki.html', encoding='utf-8') as file :  
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
# user_name = soup.find("div", class_="header__top-inner")
# print(user_name)

# social_link = soup.find(class_='header__top-logo').find_all("a")
# print(social_link)

# alla = soup.find_all('a')
# print(alla)
# for item in alla:
#     item_text = item.text
#     item_url = item.get('href')
#     print(f'{item_text}, {item_url}')

# malikoskidka = soup.find(class_='product__item').find_next_sibling().text
# print(malikoskidka)

# link22 = soup.find('a', text=re.compile('Скидка'))

# first = soup.find(class_='product__item')
# for link in links:
#     product__item_attr = link.get()

items = soup.find_all('div', class_='product__item-price')
print (items)