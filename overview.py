import sys
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
from dataclasses import astuple, dataclass

STAR_COST_TABLE = {
    'Master Agent': 25,
    'Superior Agent': 10,
    'Exceptional Agent': 7,
    'Distinguished Agent': 5
}

@dataclass
class CSGOStashItem:
    name: str
    quality: str
    price: float

    def __iter__(self):
        return (iter(astuple(self)))

    @staticmethod
    def extract_items_from_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        for item in soup.find_all('div', class_='result-box'):
            item_name = item.find_next('a').text
            item_quality = item.find_next('p').text
            try:
                item_price = item.find(lambda tag: tag.name == 'a' and '€' in tag.text).text
                item_price = float(item_price[:-1].replace(',', '.').replace('-', '0'))
            except AttributeError:
                # found an ad
                continue
            yield CSGOStashItem(item_name, item_quality, item_price)

def print_overview_for_page(csgo_stash_page_url):
    res = requests.get(csgo_stash_page_url)
    items = list(CSGOStashItem.extract_items_from_html(res.content))

    print(tabulate(items, headers=('Name', 'Quality', 'Price')))
    print('')

    merged_qualities = {}
    for item in items:
        sum_quality = merged_qualities.setdefault(item.quality, {
            'sum': 0.0,
            'count': 0
        })
        sum_quality['sum'] += item.price
        sum_quality['count'] += 1

    price_efficiencies = []
    for quality_name in merged_qualities:
        quality = merged_qualities[quality_name]
        avg_price = quality['sum'] / quality['count']
        star_cost = STAR_COST_TABLE[quality_name]
        # table rows
        price_efficiencies.append([
            quality_name,
            quality['sum'],
            quality['count'],
            avg_price,
            star_cost,
            avg_price / star_cost
        ])

    print(tabulate(price_efficiencies, headers=('Quality', 'Price Sum', 'ItemCount', 'Avg Price', 'Star cost', 'Avg Profit/Star')))
    print('')

    print('Data grabbed at {} from {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M'), csgo_stash_page_url))


if __name__=='__main__':
    if len(sys.argv) != 2:
        raise ValueError('Pass a single URL to overview.py')
    print_overview_for_page(sys.argv[1])
