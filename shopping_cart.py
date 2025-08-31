from typing import Dict

def calculate_total(cart: Dict[str, float]) -> float:
    return sum(cart.values())

def apply_discount(cart: Dict[str, float], percent: float) -> Dict[str, float]:
    factor = (100 - percent) / 100
    discounted: Dict[str, float] = {}
    for item, price in cart.items():
        discounted[item] = round(price * factor, 2)
    return discounted

def remove_item(cart: Dict[str, float], item: str) -> bool:
    if item in cart:
        del cart[item]
        return True
    return False

def most_expensive(cart: Dict[str, float]) -> str:
    if not cart:
        raise ValueError("Cart is empty")
    return max(cart, key=cart.get)

if __name__ == "__main__":
    cart = {
        "apple": 1.5,
        "bread": 2.0,
        "milk": 3.2,
        "eggs": 4.0,
    }

    # quick checks
    assert calculate_total(cart) == 10.7
    assert most_expensive(cart) == "eggs"

    discounted = apply_discount(cart, 10)
    assert discounted["apple"] == 1.35

    removed = remove_item(cart, "bread")
    assert removed is True
    assert "bread" not in cart

    print("OK")
