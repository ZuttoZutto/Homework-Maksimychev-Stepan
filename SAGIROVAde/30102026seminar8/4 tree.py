class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mirror_tree(root):
    if root is None:
        return None
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root


def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def main():
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )

    print("Preorder до зеркала: ", preorder(root))
    mirror_tree(root)
    print("Preorder после зеркала:", preorder(root))


main()