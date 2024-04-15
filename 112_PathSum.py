import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.left or root.right:
            tmp = targetSum - root.val
            l = self.hasPathSum(root.left, tmp)
            r = self.hasPathSum(root.right, tmp)
            return  l or r
        else: # situation at leaf
            return targetSum == root.val


L = [5,4,8,11,None,13,4,7,2,None,None,None,1]
sol = Solution()
tb = Tree.BuildingTree()
root = tb.Build(L)
print(sol.hasPathSum(root, 22))
