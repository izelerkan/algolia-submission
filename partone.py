import math
import json
from typing import Any

def read_data():
    with open('data/products.json', 'r') as f:
        data = json.load(f)
    
    return data


def is_camera(item) -> bool:
    item_categories = item['categories']
    return 'Cameras & Camcorders' in item_categories


data = read_data()
for item in data:
    if is_camera(item):
        item['price'] = math.floor(item['price'] - item['price'] * 0.2)


with open('data/products_discounted.json', 'w') as output_file:
    json.dump(data, output_file)
