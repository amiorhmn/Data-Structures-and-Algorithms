import pytest
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

@pytest.mark.parametrize("sorting_function", [selection_sort, bubble_sort, insertion_sort])
@pytest.mark.parametrize("input_list,expected", [
    ([3, 1, 2], [1, 2, 3]),                  # normal case
    ([], []),                                # empty list
    ([5], [5]),                              # single element
    ([2, 2, 2], [2, 2, 2]),                  # all elements same
    ([5, -1, 3], [-1, 3, 5]),                # includes negative numbers
    ([1000, 2, 300, 1], [1, 2, 300, 1000]),  # large numbers
    ([3.5, 2.1, 4.0], [2.1, 3.5, 4.0]),      # floating-point numbers
    ([1, 2, 3], [1, 2, 3]),                  # already sorted
    ([3, 2, 1], [1, 2, 3]),                  # reverse sorted
])
def test_sort(sorting_function, input_list, expected):
    assert sorting_function(input_list) == expected