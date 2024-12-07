from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        val_count = 0
        while p < len(nums) - val_count:
            if nums[p] == val:
                nums.append(val)
                del nums[p]
                val_count += 1
            else:
                p += 1
        return len(nums) - val_count