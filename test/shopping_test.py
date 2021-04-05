
from app.shopping import format_usd

def test_format_usd():
    assert format_usd(3.75838) == "$3.76"
    assert format_usd(1000000) == "$1,000,000.00"



