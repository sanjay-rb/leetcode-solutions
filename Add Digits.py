class Solution:
    def addDigits(self, num: int) -> int:
        snum = str(num)
        while len(snum) != 1:
            snum = str(sum([int(i) for i in snum]))
        return int(snum)