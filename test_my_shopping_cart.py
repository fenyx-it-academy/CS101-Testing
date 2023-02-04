from my_shopping_cart import add_to_cart, get_item, get_total_price
import pytest

def test_add_to_cart():
    cart = []
    add_to_cart(cart, "apple")
    add_to_cart(cart, "apple")
    add_to_cart(cart, "apple")
    

    with pytest.raises(OverflowError):
        add_to_cart(cart, "apple")

     

    # add_to_cart(cart, "orange")
    # assert len(cart) == 2


def test_get_item():
    cart = []
    result = get_item(cart, "orange")
    assert result == "Item not in cart."

    cart = ["orange"]
    result = get_item(cart, "orange")
    assert result == "orange"

    cart = ["orange"]
    result = get_item(cart, "banana")
    assert result == "Item not in cart."


def test_calculate_total_price_of_cart():
    cart = ["apple", "orange"]
    price_list = {
        "apple": 1.14,
        "orange": 1.50,
        "banana": 1.15
    }

    total_price = get_total_price(cart, price_list)
    assert total_price == pytest.approx(2.64)