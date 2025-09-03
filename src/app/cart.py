from __future__ import annotations
from typing import Dict
from pathlib import Path
import argparse
import sys


class ShoppingCart:
    def __init__(self) -> None:
        self.items: Dict[str, float] = {}

    def add_item(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Price must be >= 0")
        self.items[name] = price

    def remove_item(self, name: str) -> bool:
        return self.items.pop(name, None) is not None
    
    def apply_discount(self, percent: float) -> None:
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        factor = (100 - percent) / 100
        for k in list(self.items.keys()):
            self.items[k] = round(self.items[k] * factor, 2)

    def total(self) -> float:
        return round(sum(self.items.values()), 2)
    
    def most_expensive(self) -> str:
        if not self.items:
            raise ValueError("Cart is empty")
        return max(self.items, key=self.items.get)
    
    def to_file(self, path: str) -> None:
        lines = [f"{k}: {v:.2f}" for k, v in self.items.items()]
        lines.append(f"TOTAL: {self.total():.2f}")
        Path(path).write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m app.cart", description="ShoppingCart CLI")
    p.add_argument("--add", nargs=2, metavar=("ITEM", "PRICE"), action="append",
                help="Add item with price (can be repeated)")
    p.add_argument("--remove", metavar="ITEM", help="Remove an item")
    p.add_argument("--total", action="store_true", help="Show total")
    return p


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    cart = ShoppingCart()

    if args.add:
        for name, price in args.add:
            cart.add_item(name, float(price))
            print(f"Added {name} at {price}")

    if args.remove:
        print("Removed" if cart.remove_item(args.remove) else "Not found")

    if args.total:
        print(f"Total: {cart.total():.2f}")  # Keep only this line

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))