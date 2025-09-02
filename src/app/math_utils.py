# src/app/math_utils.py

import argparse
import sys

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m app.math_utils", add_help=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--fib", type=int, metavar="N", help="print Nth Fibonacci number")
    g.add_argument("--factorial", type=int, metavar="N", help="print N! (factorial)")
    g.add_argument("--is-prime", type=int, metavar="N", help="exit code 0 if prime, 1 otherwise; also prints result")
    return p

def _main(argv: list[str]) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.fib is not None:
            print(fib(args.fib))
            return 0
        if args.factorial is not None:
            print(factorial(args.factorial))
            return 0
        if args.__dict__.get("is_prime") is not None:  # handle --is-prime
            n = args.__dict__["is_prime"]
            result = is_prime(n)
            print(result)
            return 0 if result else 1
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    return 0

if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
