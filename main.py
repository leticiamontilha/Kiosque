from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab


def main():
    get_product_by_id()
    get_products_by_type()
    add_product()
    calculate_tab()
    menu_report()


if __name__ == "__main__":
    main()
