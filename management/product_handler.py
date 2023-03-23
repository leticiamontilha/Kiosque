import menu
from collections import Counter

product_list = menu.products


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")
    
    objeto = {}

    for product in product_list:
        if product["_id"] == id:
            objeto = product
    return objeto


def get_products_by_type(category: str):
    if type(category) != str:
        raise TypeError("product type must be a str")
        
    new_list = []

    for product in product_list:
        if product["type"] == category:
            new_list.append(product)
    return new_list


def add_product(menu, **kwargs):
    next_id = 0

    if len(menu) == 0:
        next_id = 1
    
    for product in menu:
        if product["_id"] >= next_id:
            next_id = product["_id"] + 1
    
    kwargs["_id"] = next_id
    menu.append(kwargs)
    return kwargs


def menu_report():
    product_count = len(product_list)
    average_price = []
    most_common_type = []
    count_type = 0
    name_type = ""

    for product in product_list:
        average_price.append(product["price"])
        most_common_type.append(product["type"])

    most_common_type = Counter(most_common_type)
    for key, value in most_common_type.items():
        if value > count_type:
            count_type = value
            name_type = key

    average_price = round(sum(average_price) / product_count, 2)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {name_type}"