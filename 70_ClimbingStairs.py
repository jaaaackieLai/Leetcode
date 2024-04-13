from math import comb
class Solution:
    def climbStairs(self, n: int) -> int:
        count, num = 1 , n // 2
        for i in range(1, num + 1):
        	count += comb(n - i, i)
        return count
        
        
# main
solution = Solution()
n = 4
res = solution.climbStairs(n)
print(res)
