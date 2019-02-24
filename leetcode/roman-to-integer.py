class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        s = s + 'I' # 随便加个a中存在的Key,防止下面a[s[i+1]] outofrange...
        for i in range(len(s)-1):
            if a[s[i]] < a[s[i+1]]:
                num -= a[s[i]]
            else:
                num += a[s[i]]
        return num


# https://leetcode-cn.com/problems/roman-to-integer/comments/