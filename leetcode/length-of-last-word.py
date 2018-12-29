'''
https://leetcode-cn.com/problems/length-of-last-word/submissions/
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        slist = s.split()
        print(slist)
        if slist == []:
            return 0
        return len(slist[-1])