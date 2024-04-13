import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    global arr
    arr = [0, 1, -1]
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.height(root)
        if res == -1:
            return False
        return True

    def height(self, root: TreeNode):
        if not root:
            return 0
        else:
            l, r = self.height(root.left), self.height(root.right)
            if l == -1 or r == -1:
                return -1
            if l-r not in arr:
                return -1
            return max(l, r) + 1

# main
tb = Tree.BuildingTree()
L = [3, 9,20,None,None, 15,7]
root = tb.Build(L)
sol = Solution()
print(sol.isBalanced(root))
