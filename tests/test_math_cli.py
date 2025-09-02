import sys
import subprocess

PY = sys.executable

def run_cli(args: list[str]) -> subprocess.CompletedProcess:
    # Runs: python -m app.math_utils <args>
    return subprocess.run(
        [PY, "-m", "app.math_utils", *args],
        capture_output=True,
        text=True,
    )

def test_fib_cli():
    p = run_cli(["--fib", "10"])
    assert p.returncode == 0
    assert p.stdout.strip() == "55"

def test_factorial_cli():
    p = run_cli(["--factorial", "5"])
    assert p.returncode == 0
    assert p.stdout.strip() == "120"

def test_is_prime_true_exit0():
    p = run_cli(["--is-prime", "97"])
    assert p.returncode == 0
    assert p.stdout.strip() == "True"

def test_is_prime_false_exit1():
    p = run_cli(["--is-prime", "100"])
    assert p.returncode == 1
    assert p.stdout.strip() == "False"

def test_negative_errors():
    p = run_cli(["--fib", "-3"])
    assert p.returncode == 2
    assert "error:" in p.stderr
