from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = [[nums[0]]]
        for index in range(0, len(nums)-1):
            if nums[index] - nums[index+1] == -1:
                result[-1].append(nums[index+1])
            else:
                result.append([nums[index+1]])
        return [f"{r[0]}->{r[-1]}" if r[0] != r[-1] else f"{r[0]}" for r in result]

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))
print(s.summaryRanges([]))