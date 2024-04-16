class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        r = rowIndex + 1
        if rowIndex < 2:
            return [1]* r
        else:
            tmp = [1,1]
            for j in range(2, r):
                tmp = self.Next_Level(tmp)
            return tmp
            
    def Next_Level(self, L:list[int]):
        n = len(L) - 1
        return [1]+[L[i]+L[i+1] for i in range(n)]+[1]

sol = Solution()
print(sol.getRow(6))
