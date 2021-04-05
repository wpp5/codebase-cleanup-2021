
from app.shopping import format_usd
from app.shopping import calculate_tax

def test_format_usd():
    assert format_usd(3.75838) == "$3.76"
    assert format_usd(1000000) == "$1,000,000.00"
    assert format_usd(0) == "$0.00"

def test_calculate_tax():
    assert calculate_tax(100) == "$8.75"

