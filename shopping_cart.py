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
