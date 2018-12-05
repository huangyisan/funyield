'''
https://leetcode-cn.com/problems/search-insert-position/
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i >= target:
                nums.insert(nums.index(i), target)
            return nums.index(target)