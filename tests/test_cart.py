# tests/test_cart.py
import pytest
from app.cart import ShoppingCart

def test_add_and_total():
    c = ShoppingCart()
    c.add_item("apple", 1.5)
    c.add_item("milk", 3.2)
    assert c.total() == 4.7

def test_remove_item():
    c = ShoppingCart()
    c.add_item("bread", 2.0)
    assert c.remove_item("bread") is True
    assert c.remove_item("bread") is False
    assert c.total() == 0.0

def test_discount_and_rounding():
    c = ShoppingCart()
    c.add_item("eggs", 4.0)
    c.add_item("milk", 3.2)
    c.apply_discount(10)
    # 4.0 -> 3.60, 3.2 -> 2.88, total = 6.48
    assert c.total() == 6.48

def test_invalid_inputs():
    c = ShoppingCart()
    with pytest.raises(ValueError):
        c.add_item("bad", -1.0)
    with pytest.raises(ValueError):
        c.apply_discount(150)

def test_most_expensive_and_empty():
    c = ShoppingCart()
    c.add_item("a", 1.0)
    c.add_item("b", 5.0)
    c.add_item("c", 3.0)
    assert c.most_expensive() == "b"
    c2 = ShoppingCart()
    with pytest.raises(ValueError):
        c2.most_expensive()

def test_to_file(tmp_path):
    c = ShoppingCart()
    c.add_item("apple", 1.5)
    c.add_item("milk", 3.2)
    p = tmp_path / "out.txt"
    c.to_file(str(p))
    content = p.read_text(encoding="utf-8")
    assert "apple: 1.50" in content
    assert "milk: 3.20" in content
    assert "TOTAL: 4.70" in content
