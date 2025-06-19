import sys

import pytest
from main import filter_data, aggregate_data, read_csv
import subprocess

sample_data = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]


def test_read_csv_file():
    data = read_csv("products.csv")
    assert data == sample_data


def test_filter_numeric_above_greater():
    result = filter_data(sample_data, "price", ">", "500")
    assert len(result) == 2
    assert result[0]["name"] == "iphone 15 pro"
    assert result[1]["name"] == "galaxy s23 ultra"


def test_filter_numeric_less_greater():
    result = filter_data(sample_data, "price", "<", "500")
    assert len(result) == 2
    assert result[0]["name"] == "redmi note 12"
    assert result[1]["name"] == "poco x5 pro"


def test_filter_text_equals():
    result = filter_data(sample_data, "brand", "=", "xiaomi")
    assert len(result) == 2


def test_aggregate_avg():
    result = aggregate_data(sample_data, "price", "avg")
    assert round(result, 2) == 674.0


def test_aggregate_min():
    result = aggregate_data(sample_data, "rating", "min")
    assert round(result, 1) == 4.4


def test_aggregate_max():
    result = aggregate_data(sample_data, "rating", "max")
    assert round(result, 1) == 4.9


def test_command_output():
    result = subprocess.run(
        [sys.executable, 'main.py', 'products.csv', '--where', 'rating', '>', '4.7'],
        capture_output=True,
        text=True
    )
    assert "iphone" in result.stdout


def test_command_output_with_aggregate():
    result = subprocess.run(
        [sys.executable, 'main.py', 'products.csv', '--where', 'rating', '>', '4.7',
         '--aggregate', 'price', 'max'],
        capture_output=True,
        text=True
    )
    assert "max" in result.stdout
    assert "1199" in result.stdout
