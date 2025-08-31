from typing import Dict

def calculate_total(cart: Dict[str, float]) -> float:
    total = 0.0
    for item, price in cart.items():
        total += price
    return total

if __name__ == "__main__":
    cart = {
        "apple": 1.5,
        "bread": 2.0,
        "milk": 3.2,
        "eggs": 4.0,
    }

    total = calculate_total(cart)
    print("Cart:", cart)
    print("Total:", total)
    assert total == 10.7
    print("OK")


def apply_discount(cart: Dict[str, float], percent: float) -> Dict[str, float]:
    factor = (100 - percent) / 100
    discounted = {}
    for item, price in cart.items():
        discounted[item] = round(price * factor, 2)
    return discounted


def remove_item(cart: Dict[str, float], item: str) -> None:
    if item in cart:
        del cart[item]


def most_expensive(cart: Dict[str, float]) -> str:
    return max(cart, key=cart.get)


if __name__ == "__main__":
    cart = {
        "apple": 1.5,
        "bread": 2.0,
        "milk": 3.2,
        "eggs": 4.0,
    }

    print("Total:", calculate_total(cart))
    print("Most expensive:", most_expensive(cart))

    discounted = apply_discount(cart, 10)
    print("With 10% discount:", discounted)

    remove_item(cart, "bread")
    print("After removing bread:", cart)
