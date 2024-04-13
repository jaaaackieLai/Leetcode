"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Do not return anything, modify nums1 in-place instead.
        k = 0 # pointer on the nums2
        if(m == 0):
            while(k != n):
                nums1.pop()
                nums1.insert(k,nums2[k])
                k += 1
        elif(n != 0):
            i = 0 # pointer on the nums1
            while(i != len(nums1)):
                if (k == n): #已經放完nums2的所有元素
                    break
                if (nums1[i] == 0 and n-k == len(nums1) - i):
                    nums1[i] = nums2[k]
                    i += 1
                    k += 1
                    continue
                if(nums2[k] <= nums1[i]): # nums2元素不大於nums1，要放
                    nums1.insert(i,nums2[k])
                    nums1.pop()
                    k += 1
                else:
                    i += 1

sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m,n = 3, 3
sol.merge(nums1, m, nums2, n)
print(nums1)
