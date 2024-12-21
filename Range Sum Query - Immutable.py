from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

        


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5)) # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5)) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3