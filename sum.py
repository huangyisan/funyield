class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            j = 1
            while j:
                print(nums[i])
                if nums[i] > target:
                    break
                if nums[i] + nums[j] == target and nums[i] != nums[j]:
                    return [i,j]
                else:
                    j+=1
                    if j==len(nums):
                        break
        return "cant find"
nums = [10,2,3,4,5,1]
target = 11
a = Solution()
print(a.twoSum(nums=nums, target=target))
