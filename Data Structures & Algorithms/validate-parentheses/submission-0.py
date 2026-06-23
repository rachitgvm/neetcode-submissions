class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack[-1]] != i:
                    return False
                stack.pop()

        return not stack