import menu

product_list = menu.products


def get_product_by_id(id):
    objeto = {}

    for product in product_list:
        if product["_id"] == id:
            objeto = product
    return objeto


def get_products_by_type(category):
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