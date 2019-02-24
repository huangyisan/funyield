class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # mapping = {"(": ")", "[": "]", "{": "}"}
        mapping = {")": "(", "]": "[", "}": "{"}
        if not s:
            return True
        for i in s:
            if i not in mapping:
                stack.append(i)
            else:
                last = stack.pop() if stack else "null"
                if last == mapping[i]:
                    continue
                else:
                    return False
        if stack:
            return False
        return True

# https://leetcode-cn.com/problems/valid-parentheses/submissions/

s = "(())"
a = Solution()
print(a.isValid(s))
