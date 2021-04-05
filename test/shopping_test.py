import os
from datetime import datetime
from pandas import read_csv
from app.shopping import format_usd, calculate_tax, lookup_product

def test_format_usd():
    assert format_usd(3.75838) == "$3.76"
    assert format_usd(1000000) == "$1,000,000.00"
    assert format_usd(0) == "$0.00"

def test_calculate_tax():
    assert calculate_tax(100) == "TAX: $8.75"

mock_products_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
mock_products_df = read_csv(mock_products_filepath)
mock_products = mock_products_df.to_dict("records")

def test_lookup_product():
    valid_result = lookup_product("8",mock_products)
    assert valid_result == {
        'aisle': 'Aisle C',
        'department': 'snacks',
        'id': 8,
        'name':'Product 8',
        'price': 10.0
    }

invalid_result = lookup_product("88888888",mock_products)
assert invalid_result == None 



