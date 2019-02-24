class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lowcase = -2147483648
        highcase = 2147483647
        if x <  lowcase or x > highcase or x == 0:
            return 0
        reversenum = int("".join(list(reversed(list(str(x))))).lstrip("0").rstrip("-"))
        if x < 0:
            return 0 if reversenum < lowcase or reversenum > highcase else 0-reversenum
        return 0 if reversenum < lowcase or reversenum > highcase else reversenum


# https://leetcode-cn.com/problems/reverse-integer/comments/