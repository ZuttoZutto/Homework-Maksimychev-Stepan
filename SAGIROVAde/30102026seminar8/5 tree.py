class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_ancestors(root, target):
    def dfs(node, path):
        if node is None:
            return None
        if node.val == target:
            return path[:]
        path.append(node.val)
        res = dfs(node.left, path)
        if res is not None:
            return res
        res = dfs(node.right, path)
        if res is not None:
            return res
        path.pop()
        return None

    return dfs(root, [])


def main():
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )

    print("Предки узла 7:", find_ancestors(root, 7))
    print("Предки узла 4:", find_ancestors(root, 4))
    print("Предки корня 1:", find_ancestors(root, 1))
    print("Предки узла 99:", find_ancestors(root, 99))


main()