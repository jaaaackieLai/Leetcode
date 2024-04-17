class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p, i = 0, prices[0]
        for j in prices[1:]:
            t = j-i
            if t>0:
                p = max(p, t)
            else:
                i = j
        return p

prices = [5,4,3,7,6,8,9,1,8,6,4,3,2,2,5,8,9]
sol = Solution()
print(prices)
print("profit is: ", sol.maxProfit(prices))
