import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        if (root):
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res
L = [1,1, 2, 3, None, 4]
tb = Tree.BuildingTree()
root = tb.Build(L)
sol = Solution()
print(sol.inorderTraversal(root))