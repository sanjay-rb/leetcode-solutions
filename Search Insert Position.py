from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right, lst, target):
            mid = (left + right) // 2

            if left > right:
                return left
            
            if lst[mid] == target:
                return mid
            
            if lst[mid] < target:
                return binarySearch(mid+1, right, lst=nums, target=target)

            if  target < lst[mid]:
                return binarySearch(left, mid-1, lst=nums, target=target)
        return binarySearch(0, len(nums)-1, lst=nums, target=target)