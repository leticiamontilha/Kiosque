import menu

product_list = menu.products


def calculate_tab(table):
    total_check = 0

    for item in table:
        for product in product_list:
            if item["_id"] == product["_id"]:
                total_check += (product["price"] * item["amount"])
        
    return {"subtotal": f"${round(total_check, 2)}"}
