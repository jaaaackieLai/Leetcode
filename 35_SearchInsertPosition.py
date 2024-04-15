class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            else:
                continue
        return len(nums)

sol = Solution()
print(sol.searchInsert([1,3,5,6], 2))
