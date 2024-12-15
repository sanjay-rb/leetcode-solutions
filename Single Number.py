from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = []
        for i in nums:
            if i in store:
                store.remove(i)
            else:
                store.append(i)
        return store[0]

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
print(s.singleNumber([-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-477]))