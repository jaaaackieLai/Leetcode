class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            i = -1
            while (digits[i] == 9):
                digits[i] = 0
                if (i+len(digits) == 0):
                    digits.append(0)
                    digits[0] = 1
                    return digits
                i -= 1
            digits[i] += 1
            return digits

# main
sol = Solution()
print(sol.plusOne([1,2,3]))
