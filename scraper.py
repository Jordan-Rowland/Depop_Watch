from bs4 import BeautifulSoup as bs
from requests import get

def return_items():
    url = 'https://www.depop.com'
    res = get(url)
    soup = bs(res.text, 'html.parser')

    raw_items = soup.select('.css-2ybrgo > a')
    imgs = soup.select('.css-2ybrgo > a > div > div > div > div')

    display_items = []

    for index, element in enumerate(raw_items):
        img = imgs[index]["data-formats"].split(",")[1].split('"')[-2]
        display_items.append(
            (f'{url}{element["href"]}',
             element.text,
             f'{img}'))

    return display_items
