import pytest
from static_array import StaticArray 

def test_insert_end():
    arr = StaticArray(3)
    arr.insert_end("a")
    arr.insert_end("b")
    assert arr.arr == ["a", "b", None]
    assert arr.length == 2

def test_insert_end_overflow():
    arr = StaticArray(2)
    arr.insert_end("a")
    arr.insert_end("b")
    with pytest.raises(OverflowError):
        arr.insert_end("c")

def test_insert_middle():
    arr = StaticArray(5)
    arr.insert_end("a")
    arr.insert_end("b")
    arr.insert_end("d")
    arr.insert_middle(2, "c")
    assert arr.arr == ["a", "b", "c", "d", None]

def test_insert_middle_greater_than_length():
    arr = StaticArray(5)
    arr.insert_end("a")
    arr.insert_end("b")
    arr.insert_middle(3, "c")
    assert arr.arr == ["a", "b", None, "c", None]

def test_insert_middle_invalid_index():
    arr = StaticArray(2)
    with pytest.raises(IndexError):
        arr.insert_middle(5, "x")

def test_insert_middle_overflow():
    arr = StaticArray(2)
    arr.insert_end("a")
    arr.insert_end("b")
    with pytest.raises(OverflowError):
        arr.insert_middle(1, "c")

def test_remove_end():
    arr = StaticArray(3)
    arr.insert_end("x")
    arr.insert_end("y")
    arr.remove_end()
    assert arr.arr == ["x", None, None]
    assert arr.length == 1

def test_remove_end_empty():
    arr = StaticArray(2)
    with pytest.raises(IndexError):
        arr.remove_end()

def test_remove_middle():
    arr = StaticArray(5)
    arr.insert_end("a")
    arr.insert_end("b")
    arr.insert_end("c")
    arr.remove_middle(1)
    assert arr.arr == ["a", "c", None, None, None]
    assert arr.length == 2

def test_remove_middle_invalid_index():
    arr = StaticArray(2)
    arr.insert_end("x")
    with pytest.raises(IndexError):
        arr.remove_middle(2)

def test_remove_middle_empty():
    arr = StaticArray(3)
    with pytest.raises(IndexError):
        arr.remove_middle(0)

def test_repr():
    arr = StaticArray(3)
    arr.insert_end("x")
    arr.insert_end("y")
    assert repr(arr) == "['x', 'y', None]"
