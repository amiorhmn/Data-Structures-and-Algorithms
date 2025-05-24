class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.value)


def pre_order_dfs(node: TreeNode):
    print(node)
    if node.left:
        pre_order_dfs(node.left)
    if node.right:
        pre_order_dfs(node.right)

def post_order_dfs(node: TreeNode):
    if node.left:
        post_order_dfs(node.left)
    if node.right:
        post_order_dfs(node.right)
    print(node)

def in_order_dfs(node: TreeNode):
    if node.left:
        in_order_dfs(node.left)
    print(node)
    if node.right:
        in_order_dfs(node.right)

def level_order_bfs(node: TreeNode):
    queue = [node]
    while queue:
        curr = queue.pop(0)
        print(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


# Time Complexity:
# pre-order     O(n)
# post-order    O(n)
# in-order      O(n)
# level-order   O(n)