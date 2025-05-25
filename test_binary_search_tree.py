import pytest
from binary_search_tree import bst_remove, TreeNode, bst_insert, bst_contains, bst_find, bst_max, bst_min

def build_bst_from_list(values):
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


def test_insert_into_empty_tree():
    root = None
    root = bst_insert(root, 10)
    assert root is not None
    assert root.value == 10
    assert root.left is None
    assert root.right is None

def test_insert_smaller_and_larger():
    root = None
    root = bst_insert(root, 10)
    root = bst_insert(root, 5)
    root = bst_insert(root, 15)
    assert inorder_traversal(root) == [5, 10, 15]

def test_insert_duplicate_value():
    root = None
    root = bst_insert(root, 10)
    root = bst_insert(root, 10)
    # Depending on implementation, duplicate goes to right
    assert inorder_traversal(root) == [10, 10]

def test_insert_multiple_values():
    vals = [10, 5, 15, 2, 7, 12, 18]
    root = None
    for v in vals:
        root = bst_insert(root, v)
    assert inorder_traversal(root) == sorted(vals)

def test_insert_negative_and_float():
    root = None
    root = bst_insert(root, 10)
    root = bst_insert(root, -5)
    root = bst_insert(root, 7.5)
    root = bst_insert(root, 20)
    assert inorder_traversal(root) == [-5, 7.5, 10, 20]

def test_insert_chain_left():
    root = None
    for v in [10, 9, 8, 7, 6]:
        root = bst_insert(root, v)
    assert inorder_traversal(root) == [6, 7, 8, 9, 10]

def test_insert_chain_right():
    root = None
    for v in [10, 11, 12, 13, 14]:
        root = bst_insert(root, v)
    assert inorder_traversal(root) == [10, 11, 12, 13, 14]

def test_insert_edge_case_between_nodes():
    # This tests the special insertion logic in the implementation
    root = None
    root = bst_insert(root, 10)
    root = bst_insert(root, 5)
    root = bst_insert(root, 7)  # Should be inserted between 5 and 10
    assert inorder_traversal(root) == [5, 7, 10]


def test_bst_contains():
    root = build_bst_from_list([10, 5, 15])
    assert bst_contains(root, 10)
    assert bst_contains(root, 5)
    assert bst_contains(root, 15)
    assert not bst_contains(root, 7)
    assert not bst_contains(None, 1)

def test_bst_find():
    root = build_bst_from_list([10, 5, 15])
    node = bst_find(root, 5)
    assert node is not None and node.value == 5
    assert bst_find(root, 100) is None
    assert bst_find(None, 1) is None

def test_bst_min_max():
    vals = [10, 5, 15, 3, 7, 12, 18]
    root = build_bst_from_list(vals)
    assert bst_min(root).value == 3
    assert bst_max(root).value == 18
    # Single node
    single = TreeNode(42)
    assert bst_min(single).value == 42
    assert bst_max(single).value == 42


def test_remove_from_empty_tree():
    assert bst_remove(None, 5) is None

def test_remove_only_node():
    root = TreeNode(10)
    assert bst_remove(root, 10) is None

def test_remove_leaf_node():
    root = build_bst_from_list([10, 5, 15])
    root = bst_remove(root, 5)
    assert inorder_traversal(root) == [10, 15]
    root = bst_remove(root, 15)
    assert inorder_traversal(root) == [10]

def test_remove_node_with_one_left_child():
    root = build_bst_from_list([10, 5])
    root = bst_remove(root, 10)
    assert inorder_traversal(root) == [5]

def test_remove_node_with_one_right_child():
    root = build_bst_from_list([10, 15])
    root = bst_remove(root, 10)
    assert inorder_traversal(root) == [15]

def test_remove_node_with_two_children():
    root = build_bst_from_list([10, 5, 15, 12, 18])
    root = bst_remove(root, 15)
    assert inorder_traversal(root) == [5, 10, 12, 18]
    root = bst_remove(root, 10)
    assert inorder_traversal(root) == [5, 12, 18]

def test_remove_root_with_two_children():
    root = build_bst_from_list([10, 5, 15, 12, 18])
    root = bst_remove(root, 10)
    assert inorder_traversal(root) == [5, 12, 15, 18]

def test_remove_nonexistent_value():
    root = build_bst_from_list([10, 5, 15])
    orig = inorder_traversal(root)
    root = bst_remove(root, 99)
    assert inorder_traversal(root) == orig

def test_remove_minimum_node():
    root = build_bst_from_list([10, 5, 15, 2])
    root = bst_remove(root, 2)
    assert inorder_traversal(root) == [5, 10, 15]

def test_remove_maximum_node():
    root = build_bst_from_list([10, 5, 15, 20])
    root = bst_remove(root, 20)
    assert inorder_traversal(root) == [5, 10, 15]

def test_remove_all_nodes_one_by_one():
    vals = [10, 5, 15, 2, 7, 12, 18]
    root = build_bst_from_list(vals)
    for v in sorted(vals):
        root = bst_remove(root, v)
    assert root is None

