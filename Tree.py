from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BuildingTree:
    def Build(self, L, i=0):
        if i < len(L) and L[i] is not None:  # Check if the current index is within bounds and not None
            node = TreeNode(L[i])
            node.left = self.Build(L, 2*i + 1)  # Recursive call for the left child
            node.right = self.Build(L, 2*i + 2)  # Recursive call for the right child
            return node
        return None  # Return None if the index is out of bounds or L[i] is None

    def printLevelOrder(self,root):
        if not root:
            print("The tree is empty.")
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                print(node.val, end=' ')
                queue.append(node.left)
                queue.append(node.right)
            else:
                print("None", end=' ')
        print()



