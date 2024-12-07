from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            balance = target - nums[i]
            next_nums = nums[i+1:]
            if balance in next_nums:
                return [i, next_nums.index(balance)+(i+1)]