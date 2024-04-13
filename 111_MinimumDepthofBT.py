import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: # empty tree
            return 0
        if not (root.left or root.right): # 左右皆空
            return 1
        if not root.left: #only left is None
            return 1 + self.minDepth(root.right)
        if not root.right: # only right is None
            return 1 + self.minDepth(root.left)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
L = [1,2,20,None,None,3]
tree_builder = Tree.BuildingTree()
root = tree_builder.Build(L)
sol = Solution()
print(sol.minDepth(root))