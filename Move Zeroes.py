from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
s = Solution()
s.moveZeroes([0,1,0,3,12])