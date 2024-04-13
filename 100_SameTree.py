import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q: # 2棵樹都有東西
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            else :
                return False
        elif not(p or q) : # 2邊都是空的
            return True
        else:
            return False

#main
tb = Tree.BuildingTree()
L1 = [1,None,2]
L2 = [1,2,None]
r1 = tb.Build(L1)
r2 = tb.Build(L2)

L3 = [3, None, 4, None, None, 4, None]
L4 = [3, None, 4, None, None, 4, None]
r3 = tb.Build(L3)
r4 = tb.Build(L4)

# Expected: False, True
sol = Solution()
print(sol.isSameTree(r1,r2))
print(sol.isSameTree(r3,r4))
