class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return list(set(nums))

nums = [1,1,2]
a = Solution()
print(a.removeDuplicates(nums))
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/