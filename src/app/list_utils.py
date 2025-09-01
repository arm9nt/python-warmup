from typing import Iterable, List

def unique(sorted_items: Iterable[int]) -> List[int]:
    """Return unique items from a sorted iterable, preserving order."""
    out: List[int] = []
    prev = object()
    for x in sorted_items:
        if x != prev:
            out.append(x)
            prev = x
    return out
