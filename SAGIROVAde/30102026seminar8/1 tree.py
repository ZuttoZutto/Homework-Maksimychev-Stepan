class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _is_mirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (
        a.val == b.val
        and _is_mirror(a.left, b.right)
        and _is_mirror(a.right, b.left)
    )


def is_symmetric(root):
    if root is None:
        return True
    return _is_mirror(root.left, root.right)


def main():
    symmetric_root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )

    asymmetric_root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), None),
        TreeNode(2, None, None)
    )

    print("Симметричное дерево:", is_symmetric(symmetric_root))
    print("Несимметричное дерево:", is_symmetric(asymmetric_root))


main()