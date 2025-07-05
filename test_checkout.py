from checkout import Checkout


def test_add_item_to_cart():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    checkout.add_item_to_cart("eggs")
    assert "eggs" in checkout.cart


def test_add_item_to_cart_item_not_available():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    checkout.add_item_to_cart("bread")
    assert "bread" not in checkout.cart


def test_get_cart_total_1_item():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    checkout.add_item_to_cart("eggs")
    assert checkout.get_cart_total() == 1.8


def test_get_cart_total_3_items():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    checkout.add_item_to_cart("eggs")
    checkout.add_item_to_cart("coke")
    checkout.add_item_to_cart("coffee")
    assert checkout.get_cart_total() == 7.7


def test_get_cart_total_empty_cart():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    assert checkout.get_cart_total() == 0


def test_empty_cart():
    items = {
        "diet_coke": {
            "price": 1.1
        },
        "coke": {
            "price": 1.2
        },
        "eggs": {
            "price": 1.8
        },
        "coffee": {
            "price": 4.7
        }
    }
    checkout = Checkout(items)
    checkout.add_item_to_cart("eggs")
    checkout.add_item_to_cart("coke")
    checkout.add_item_to_cart("coffee")
    checkout.empty_cart()
    assert checkout.cart == []
