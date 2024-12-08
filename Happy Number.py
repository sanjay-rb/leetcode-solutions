class Solution:
    def isHappy(self, n: int) -> bool:
        sn = str(n)
        buffer = [sn]
        while True:
            sn = str(sum([int(i)**2 for i in sn]))
            if sn == "1":
                return True
            if sn in buffer:
                return False
            buffer.append(sn)
# s = Solution()
# print(s.isHappy(19))
# print(s.isHappy(2))
