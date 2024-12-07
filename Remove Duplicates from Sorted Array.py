from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = sorted(set(nums))
        k = len(temp)
        for i in range(k):
            nums[i] = temp[i]
        return k