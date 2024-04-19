from functools import reduce
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        def op(x,y):
            return x ^ y
        if len(nums) == 1:
            return nums[0]
        else:
            # 出現2次就會消掉 -> XOR
            tmp = reduce(op, nums)
            return tmp

sol = Solution()
L = [2,2,1,1,4]
print(sol.singleNumber(L))