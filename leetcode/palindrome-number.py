'''
https://leetcode-cn.com/problems/palindrome-number/description/
12321
12321 / 10 = 1232 .. 1
12321 / 100 = 123 .. 21
12321 / 1000 = 12 .. 321
12321 / 10000 = 1 .. 2321
'''
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        """

        if x < 0:
            return False
        if self.successive_division(x) == list(reversed(self.successive_division(x))):
            return True
        return False

    def get_count(self, x):
        '''

        :param x:
        :return: x是几位数
        '''
        y = 10
        while True:
            if x // y == 0:
                break
            y *= 10
        z = math.log10(y)
        return int(z)

    def successive_division(self, x):
        '''
        :param x:
        :return: 辗转相除余数列表
        '''
        c = []
        for i in range(self.get_count(x)-1,-1,-1):
            const = 10
            const = math.pow(const, i)
            x, const, z = x % const, const, x // const
            c.append(int(z))
        return c

a = Solution()
print(a.isPalindrome(1369229631))




