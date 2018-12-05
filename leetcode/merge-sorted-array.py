'''
https://leetcode-cn.com/problems/merge-sorted-array/
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
p=Solution()
p.merge(nums1=nums1,nums2=nums2,m=m,n=n)