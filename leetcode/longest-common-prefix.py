class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = []
        num = 0
        while True:
            try:
                if len(set(list(map(lambda x: x[num], strs)))) == 1:
                    prefix.append(strs[0][num])
                    num +=1
                else:
                    if prefix:
                        return "".join(prefix)

                    else:
                        return ""
            except:
                return "".join(prefix)


#
str = ["flower","flow","flight"]
a = Solution()
print(a.longestCommonPrefix(str))



# https://leetcode-cn.com/problems/longest-common-prefix/