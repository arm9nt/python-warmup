from typing import Iterable, List

def sum_list(nums: Iterable[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total

def filter_evens(nums: Iterable[int]) -> List[int]:
    evens: List[int] = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens

if __name__ == "__main__":
    data = [3, 8, 1, 14, 5, 10]
    assert sum_list(data) == 41
    assert filter_evens(data) == [8, 14, 10]
    print("OK")
