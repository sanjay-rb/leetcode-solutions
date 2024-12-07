from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return_str = ""
        len_strs = [len(i) for i in strs]
        min_str = strs[len_strs.index(min(len_strs))]
    
        for i in range(len(min_str)):
            l = min_str[i]
            flag = True
            for s in strs:
                if l != s[i]:
                    flag = False
                    break
            
            if flag:
                return_str += l
            else:
                return return_str
        return return_str