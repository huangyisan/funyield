class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
            print(a)
        return a

a = Solution()
nums1 = [1,3,3,4,5,7,1,5,7]
nums = [4,1,2,1,2]
print(a.singleNumber(nums1))