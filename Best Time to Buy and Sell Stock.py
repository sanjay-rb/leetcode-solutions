from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        values = {}
        current_min = prices[0]
        max_list = []
        for current_value in prices[1:]:
            if current_min > current_value:
                values[current_min] = max_list
                current_min = current_value
                max_list = []
            else:
                max_list.append(current_value)
        values[current_min] = max_list

        max_profit = 0
        for key, value in values.items():
            if value:
                diff = max(value) - key
                if max_profit < diff:
                    max_profit = diff
        return max_profit




s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,4,1]))