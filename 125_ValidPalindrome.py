class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.Convert(s)
        return s[::-1] == s

    def Convert(self, s: str) -> str:
        arr = "".join(i for i in s if i.isalpha() or i.isdigit()).lower()
        
        return arr

sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))       