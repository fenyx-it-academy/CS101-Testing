cart = []

price_list = {"apple": 1.05, "banana": 1.10, "orange": 1.25}


def add_to_cart(cart, item, limit=3):

    if len(cart) == limit:
        raise OverflowError("you cannot add any more items.")
    
    cart.append(item)  # ['apple']
    return len(cart)  # 1


def get_item(cart, item):
    if item in cart:
        return item

    return "Item not in cart."


def get_total_price(cart, price_list):
    total_price = 0

    for item in cart:

        total_price += price_list[item]
    return total_price
