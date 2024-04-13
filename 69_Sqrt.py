class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        l, r = 1 , x
        while (l <= r):
            mid = (l+r) // 2
            sqare = mid * mid
            if (sqare == x):
                return mid
            elif (sqare < x):
                if (mid + 1)*(mid + 1) > x:
                    return mid
                else:
                    l = mid + 1
            elif (sqare > x):
                r = mid - 1

# main
sol = Solution()
print(sol.mySqrt(4))
