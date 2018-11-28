class Solution(object):
    def twoSum(self, nums, target):
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
nums = [3,2,4]
target = 6
a = Solution()
print(a.twoSum(nums=nums, target=target))
