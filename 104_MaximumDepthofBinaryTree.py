import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#main
List = [1,2,2,3]
tb = Tree.BuildingTree()
root = tb.Build(List)

sol = Solution()
print(sol.maxDepth(root))
