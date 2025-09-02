from __future__ import annotations
from typing import Dict

class ShoppingCart:
    def __init__(self) -> None:
        self.items: Dict[str, float] = {}

    def add_item(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Price must be >= 0")
        self.items[name] = price

    def remove_item(self, name: str) ->bool:
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
            return ValueError("Cart is empty")
        return max(self.items, key=self.items.get)
    
    def to_file(self, path: str) -> None:
        from pathlib import Path
        lines = [f"{k}: {v:.2f}" for k, v in self.items.items()]
        lines.append(f"Total: {self.total():.2f}")
        Path(path).write_text("\n".join(lines), encoding="utf-8")
