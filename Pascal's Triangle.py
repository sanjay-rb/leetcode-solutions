from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [i*[1] for i in range(1, numRows+1)]
        for row_index in range(2, len(rows)):
            row = rows[row_index]
            leng = len(row)
            for value_index in range(1, leng-1):
                row[value_index] = rows[row_index-1][value_index-1] + rows[row_index-1][value_index]
        return rows
s = Solution()
s.generate(5)