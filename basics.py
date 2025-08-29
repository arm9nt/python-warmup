def reserve_string(s: str) -> str:
    return s[::-1]

def is_even(n: int) -> bool:
    return n % 2 == 0

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in text.split():
        counts[w] = counts.get(w, 0) + 1
    return counts

if __name__ == "__main__":
    print(reserve_string("hello"))
    print(is_even(7))
    print(word_count("I love Python Python"))
