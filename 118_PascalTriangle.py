class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows >2:
            tmp = [1,1]
            res = [[1],[1,1]]
            for j in range(2, numRows):
                tmp = self.Next_Level(tmp)
                res.append(tmp)
            return res
        else:
            return [[1]*n for n in range(1, numRows+1)]
            
    def Next_Level(self, L:list[int]):
        n = len(L) - 1
        return [1]+[L[i]+L[i+1] for i in range(n)]+[1]

sol = Solution()
print(sol.generate(5))
