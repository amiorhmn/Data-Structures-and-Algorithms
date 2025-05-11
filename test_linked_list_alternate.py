import pytest
from linked_list_alternate import LinkedList

@pytest.fixture
def linked_list():
    ll = LinkedList()
    ll.append("A")
    ll.append("B")
    ll.append("C")
    return ll

def test_append(linked_list):
    assert len(linked_list) == 3
    assert repr(linked_list) == "A, B, C"
    assert linked_list.get_value(0) == "A"
    assert linked_list.get_value(1) == "B"
    assert linked_list.get_value(2) == "C"
    assert linked_list.head.next.value == "A"
    assert linked_list.tail.value == "C"
    with pytest.raises(IndexError) as e:
        linked_list.get_value(3)
    assert str(e.value) == "Index 3 does not exist"

def test_prepend(linked_list):
    linked_list.prepend("Start")
    assert len(linked_list) == 4
    assert linked_list.get_value(0) == "Start"
    assert repr(linked_list) == "Start, A, B, C"
    assert linked_list.head.next.value == "Start"

def test_insert_middle(linked_list):
    linked_list.insert(2, "X")
    assert len(linked_list) == 4
    assert linked_list.get_value(2) == "X"
    assert linked_list.get_value(1) == "B"
    assert linked_list.get_value(3) == "C"
    assert repr(linked_list) == "A, B, X, C"

def test_insert_head(linked_list):
    linked_list.insert(0, "X")
    assert len(linked_list) == 4
    assert linked_list.get_value(0) == "X"
    assert linked_list.get_value(2) == "B"
    assert linked_list.get_value(3) == "C"
    assert repr(linked_list) == "X, A, B, C"
    assert linked_list.head.next.value == "X"

def test_insert_tail(linked_list):
    linked_list.insert(3, "X")
    assert len(linked_list) == 4
    assert linked_list.get_value(3) == "X"
    assert linked_list.get_value(1) == "B"
    assert linked_list.get_value(2) == "C"
    assert repr(linked_list) == "A, B, C, X"
    assert linked_list.tail.value == "X"

def test_insert_outside(linked_list):
    with pytest.raises(IndexError) as e:
        linked_list.insert(4, "X")
    assert str(e.value) == "Cannot insert at index 4"

def test_set_value(linked_list):
    linked_list.set_value(1, "Z")
    assert linked_list.get_value(1) == "Z"
    assert repr(linked_list) == "A, Z, C"
    with pytest.raises(IndexError) as e:
        linked_list.set_value(3, "Y")
    assert str(e.value) == "Index 3 does not exist"

def test_pop(linked_list):
    popped = linked_list.pop()
    assert popped == "C"
    assert len(linked_list) == 2
    assert linked_list.get_value(1) == "B"
    assert repr(linked_list) == "A, B"
    assert linked_list.tail.value == "B"

def test_shift(linked_list):
    shifted = linked_list.shift()
    assert shifted == "A"
    assert len(linked_list) == 2
    assert linked_list.get_value(0) == "B"
    assert repr(linked_list) == "B, C"
    assert linked_list.head.next.value == "B"

def test_remove_middle(linked_list):
    linked_list.remove(1)
    assert len(linked_list) == 2
    assert linked_list.get_value(1) == "C"
    assert repr(linked_list) == "A, C"

def test_remove_head(linked_list):
    linked_list.remove(0)
    assert len(linked_list) == 2
    assert linked_list.get_value(0) == "B"
    assert repr(linked_list) == "B, C"
    assert linked_list.head.next.value == "B"

def test_remove_tail(linked_list):
    linked_list.remove(2)
    assert len(linked_list) == 2
    assert linked_list.get_value(1) == "B"
    assert repr(linked_list) == "A, B"
    assert linked_list.tail.value == "B"

def test_remove_outside(linked_list):
    with pytest.raises(IndexError) as e:
        linked_list.remove(3)
    assert str(e.value) == "Index 3 does not exist"

def test_remove_all(linked_list):
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)
    assert len(linked_list) == 0
    assert linked_list.head.next == None
    assert linked_list.tail.value == None

def test_pop_all(linked_list):
    linked_list.pop()
    linked_list.pop()
    linked_list.pop()
    assert len(linked_list) == 0
    assert repr(linked_list) == ""
    assert linked_list.head.next == None
    assert linked_list.tail.value == None

def test_shift_all(linked_list):
    linked_list.shift()
    linked_list.shift()
    linked_list.shift()
    assert len(linked_list) == 0
    assert repr(linked_list) == ""
    assert linked_list.head.next == None
    assert linked_list.tail.value == None



@pytest.fixture
def empty_linked_list():
    ll = LinkedList()
    return ll

def test_empty_ll(empty_linked_list):
    assert len(empty_linked_list) == 0
    assert repr(empty_linked_list) == ""

def test_empty_pop(empty_linked_list):
    with pytest.raises(IndexError) as e:
        empty_linked_list.pop()
    assert str(e.value) == "Cannot pop from empty list"

def test_empty_shift(empty_linked_list):
    with pytest.raises(IndexError) as e:
        empty_linked_list.shift()
    assert str(e.value) == "Cannot shift from empty list"

def test_empty_remove(empty_linked_list):
    with pytest.raises(IndexError) as e:
        empty_linked_list.remove(0)
    assert str(e.value) == "Cannot shift from empty list"



def test_reverse():
    ll_empty = LinkedList()
    assert len(ll_empty.reverse()) == 0
    assert repr(ll_empty.reverse()) == ""
    
    ll_1 = LinkedList()
    ll_1.append("A")
    assert repr(ll_1.reverse()) == "A"

    ll_2 = LinkedList()
    ll_2.append("A")
    ll_2.append("B")
    assert repr(ll_2.reverse()) == "B, A"
    assert ll_2.head.next.value == "B"
    assert ll_2.tail.value == "A"

    ll_3 = LinkedList()
    ll_3.append("A")
    ll_3.append("B")
    ll_3.append("C")
    assert repr(ll_3.reverse()) == "C, B, A"
    assert ll_3.head.next.value == "C"
    assert ll_3.tail.value == "A"

    ll_4 = LinkedList()
    ll_4.append("A")
    ll_4.append("B")
    ll_4.append("C")
    ll_4.append("D")
    assert repr(ll_4.reverse()) == "D, C, B, A"
    assert ll_4.head.next.value == "D"
    assert ll_4.tail.value == "A"

    ll_7 = LinkedList()
    ll_7.append("A")
    ll_7.append("B")
    ll_7.append("C")
    ll_7.append("D")
    ll_7.append("E")
    ll_7.append("F")
    ll_7.append("G")
    assert repr(ll_7.reverse()) == "G, F, E, D, C, B, A"
    assert ll_7.head.next.value == "G"
    assert ll_7.tail.value == "A"