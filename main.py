from management.product_handler import get_product_by_id, get_products_by_type, add_product
from management.tab_handler import calculate_tab

def main():
    get_product_by_id()
    get_products_by_type()
    add_product()
    calculate_tab()


if __name__ == "__main__":
    # print(get_product_by_id(250))
    # print(get_products_by_type("vegetable"))
    main()
