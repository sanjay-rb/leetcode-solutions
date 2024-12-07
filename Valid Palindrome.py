class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = ''.join([i for i in s if i.isalnum()])
        print(f, f[::-1])
        return f == f[::-1]