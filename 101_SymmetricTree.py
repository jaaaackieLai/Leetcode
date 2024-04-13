import Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    	 	
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 and t2 and t1.val == t2.val:
            return self.isSymmetricTree(t1.left, t2.right) and self.isSymmetricTree(t1.right, t2.left)
        elif not(t1 or t2):
            return True
        return False
        
#main
tb = Tree.BuildingTree()
List = [1,2,2,3,None, None, 3]
root = tb.Build(List)

sol = Solution()
print(sol.isSymmetric(root))
