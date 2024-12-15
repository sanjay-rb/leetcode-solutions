from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for value in set(nums):
            if nums.count(value) > len(nums)/2:
                return value

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))