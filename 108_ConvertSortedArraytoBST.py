class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.build(nums, 0, len(nums))

    def build(self, nums, l, r):
        if l > r :
            return None
        m = (l + r) // 2
        root = TreeNode(nums[m])
        if m != l:
            root.left = self.build(nums, l, m)
        if r != m + 1:
            root.right = self.build(nums, m+1, r)
        return root

sol = Solution()
nums = [-10,-3,0,1,3,5]
root = sol.sortedArrayToBST(nums)
print(root.val)
        
