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