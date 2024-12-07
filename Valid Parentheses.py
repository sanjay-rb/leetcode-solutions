class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        for i in s:
            if not stack:
                stack.append(i)
                continue

            if i in brackets.values():
                stack.append(i)
            else:
                if stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack) == 0