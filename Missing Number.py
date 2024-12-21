from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_n_number = n*(n+1)//2
        for i in nums:
            sum_of_n_number-=i
        return sum_of_n_number

s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))