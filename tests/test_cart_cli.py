import sys
import subprocess

PY = sys.executable

def run_cli(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [PY, "-m", "app.cart", *args],
        capture_output=True,
        text=True,
    )

def test_cart_add_and_total():
    p = run_cli(["--add", "apple", "1.5", "--add", "milk", "3.2", "--total"])
    assert p.returncode == 0
    out = p.stdout.strip()
    assert "Added apple" in out
    assert "Added milk" in out
    assert "Total: 4.7" in out


def test_cart_remove_item():
    p = run_cli([
        "--add", "bread", "2.0",
        "--remove", "bread",
        "--total"
    ])
    assert p.returncode == 0
    out = p.stdout.strip()
    assert "Added bread" in out
    assert "Removed" in out
    assert "Total: 0.0" in out
