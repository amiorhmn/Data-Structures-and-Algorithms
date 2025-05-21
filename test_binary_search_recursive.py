import pytest
from binary_search_recursive import binary_search

def test_empty_array():
    assert binary_search([], 1) == -1, "Empty array should return -1"

def test_single_element_found():
    assert binary_search([1], 1) == 0, "Single element array with target should return 0"

def test_single_element_not_found():
    assert binary_search([1], 2) == -1, "Single element array without target should return -1"

def test_target_at_start():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Target at start should return 0"

def test_target_at_end():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4, "Target at end should return 4"

def test_target_in_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2, "Target in middle should return correct index"

def test_target_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Target not in array should return -1"
    assert binary_search([1, 2, 3, 4, 5], 0) == -1, "Target less than smallest element should return -1"

def test_duplicate_elements():
    # For arrays with duplicates, binary search may return any valid index
    result = binary_search([1, 2, 2, 2, 3], 2)
    assert result in [1, 2, 3], "Duplicate target should return a valid index"

def test_even_length_array():
    assert binary_search([1, 2, 3, 4], 3) == 2, "Even-length array target found"
    assert binary_search([1, 2, 3, 4], 5) == -1, "Even-length array target not found"

def test_odd_length_array():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3, "Odd-length array target found"
    assert binary_search([1, 2, 3, 4, 5], 0) == -1, "Odd-length array target not found"

def test_large_array():
    large_arr = list(range(1000))
    assert binary_search(large_arr, 999) == 999, "Large array target at end"
    assert binary_search(large_arr, 500) == 500, "Large array target in middle"
    assert binary_search(large_arr, 1000) == -1, "Large array target not found"

def test_negative_numbers():
    assert binary_search([-5, -3, -1, 0, 2], -3) == 1, "Negative numbers target found"
    assert binary_search([-5, -3, -1, 0, 2], -4) == -1, "Negative numbers target not found"

def test_all_same_elements():
    assert binary_search([2, 2, 2, 2], 2) in [0, 1, 2, 3], "Array with all same elements should return valid index"
    assert binary_search([2, 2, 2, 2], 3) == -1, "Array with all same elements, target not found"

def test_sorted_floating_point():
    assert binary_search([1.1, 2.2, 3.3, 4.4], 2.2) == 1, "Floating point target found"
    assert binary_search([1.1, 2.2, 3.3, 4.4], 2.3) == -1, "Floating point target not found"