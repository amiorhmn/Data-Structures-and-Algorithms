import pytest
from binary_tree import TreeNode, pre_order_dfs, post_order_dfs, in_order_dfs, level_order_bfs

def build_sample_tree():
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def test_post_order_dfs_balanced_tree(capsys):
    root = build_sample_tree()
    post_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    # Should print 4, 5, 2, 3, 1
    assert captured == ['4', '5', '2', '3', '1']

def test_post_order_dfs_single_node(capsys):
    root = TreeNode(42)
    post_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['42']

def test_post_order_dfs_empty_tree():
    with pytest.raises(AttributeError):
        post_order_dfs(None)

def test_post_order_dfs_left_skewed(capsys):
    # 1 -> 2 -> 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    post_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['3', '2', '1']

def test_post_order_dfs_right_skewed(capsys):
    # 1 -> 2 -> 3 (all right)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    post_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['3', '2', '1']

def test_pre_order_dfs_balanced_tree(capsys):
    root = build_sample_tree()
    pre_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    # Should print 1, 2, 4, 5, 3
    assert captured == ['1', '2', '4', '5', '3']

def test_pre_order_dfs_single_node(capsys):
    root = TreeNode(99)
    pre_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['99']

def test_pre_order_dfs_empty_tree():
    with pytest.raises(AttributeError):
        pre_order_dfs(None)

def test_pre_order_dfs_left_skewed(capsys):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    pre_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['1', '2', '3']

def test_pre_order_dfs_right_skewed(capsys):
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    pre_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['1', '2', '3']

def test_in_order_dfs_balanced_tree(capsys):
    root = build_sample_tree()
    in_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    # Should print 4, 2, 5, 1, 3
    assert captured == ['4', '2', '5', '1', '3']

def test_in_order_dfs_single_node(capsys):
    root = TreeNode(7)
    in_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['7']

def test_in_order_dfs_empty_tree():
    with pytest.raises(AttributeError):
        in_order_dfs(None)

def test_in_order_dfs_left_skewed(capsys):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    in_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['3', '2', '1']

def test_in_order_dfs_right_skewed(capsys):
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    in_order_dfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['1', '2', '3']

def test_level_order_bfs_balanced_tree(capsys):
    root = build_sample_tree()
    level_order_bfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    # Should print 1, 2, 3, 4, 5
    assert captured == ['1', '2', '3', '4', '5']

def test_level_order_bfs_single_node(capsys):
    root = TreeNode(8)
    level_order_bfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['8']

def test_level_order_bfs_empty_tree():
    with pytest.raises(AttributeError):
        level_order_bfs(None)

def test_level_order_bfs_left_skewed(capsys):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    level_order_bfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['1', '2', '3']

def test_level_order_bfs_right_skewed(capsys):
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    level_order_bfs(root)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['1', '2', '3']