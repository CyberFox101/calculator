import pytest
from batch_calculator import process_calculation

def test_multiply_batch():

    test_result_multiply = process_calculation("multiply", "9", "7")
    assert test_result_multiply == ("OK", 63.0, "")
