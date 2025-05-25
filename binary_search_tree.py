class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.value)


# takes root node of a BST, inserts a new node containg val at appropriate position and returns the root of the BST
def bst_insert(root: TreeNode | None, val: int | float) -> TreeNode:
    if root is None:
        root = TreeNode(val)
        return root
    
    curr = root
    while curr:
        if val < curr.value:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right

    return root

     
# returns true if the BST contains val, otherwise returns false
def bst_contains(root: TreeNode | None, val: int | float) -> bool:
    while root:
        if val < root.value:
            root = root.left
        elif val > root.value:
            root = root.right
        else:
            return True
    return False


# if val is present in the BST, returns the node containing val, otherwise returns None
def bst_find(root: TreeNode | None, val: int | float) -> TreeNode | None:
    while root:
        if val < root.value:
            root = root.left
        elif val > root.value:
            root = root.right
        else:
            return root
    return None


# returns the node containg the minimum value in a BST
def bst_min(root: TreeNode) -> TreeNode:
    while root.left:
        root = root.left
    return root


# returns the node containg the maximum value in a BST
def bst_max(root: TreeNode) -> TreeNode:
    while root.right:
        root = root.right
    return root


# if present, removes the node containing val from the input BST and returns the root of the BST
def bst_remove(root: TreeNode | None, val: int | float) -> TreeNode | None:
    if root is None:
        return None
    
    if val < root.value:
        root.left =  bst_remove(root.left, val)     # replace the current left subtree with the left subtree but the 'val' node removed
    elif val > root.value:
        root.right =  bst_remove(root.right, val)   # replace the current right subtree with the right subtree but the 'val' node removed
    else:   # if val == root.value
        if root.left is None:   # this also covers the case where both children nodes are None (i.e. root.left and root.right are None)
            return root.right
        if root.right is None:
            return root.left
        succ = bst_min(root.right)  # the in-order successor of root (i.e. minimum node of the right subtree)
        root.value = succ.value     # replace the value of root with the value of successor
        root.right = bst_remove(root.right, succ.value)     # remove the successor node (i.e. replace the current right subtree with right subtree but successor node removed)

    return root