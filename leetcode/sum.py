'''
https://leetcode-cn.com/problems/two-sum/description/
'''

class Solution(object):
    def twoSum(self, nums, target):

        '''
        d ={}
        for i,k in enumerate(nums):
            j = target - k
            if j in d:
                return [i,d[j]]
            else:
                d[j] = i
        '''
        for i in range(0,len(nums)):
            while True:
                other_num = target - nums[i]
                try:
                    other_num_index = nums.index(other_num)
                except Exception:
                    break
                else:
                    if i == other_num_index:
                        break
                    return [i,other_num_index]
        return "cant find"
nums = [3,3,2,4]
target = 6
a = Solution()
print(a.twoSum(nums=nums, target=target))
