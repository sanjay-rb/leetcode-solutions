class Solution:
    def romanToInt(self, s: str) -> int:   
        r_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        num = 0

        for i in range(len(s)):
            num += r_map[s[i]]
            
            if i == 0:
                continue

            if r_map[s[i-1]] < r_map[s[i]]:
                num -= r_map[s[i]] + r_map[s[i-1]]
                num += r_map[s[i]] - r_map[s[i-1]]


        return num