class Solution:
    def sumOddLengthSubarrays(self, arr:list) -> int:

        ans = 0
        for n in range(1, len(arr) + 1, 2):
            print(n)
            for i in range(len(arr) - n + 1):
                print(len(arr)-n+1)
                print(arr[i: i + n])
                ans += sum(arr[i: i + n])
        print(ans)
        return ans


a = Solution()
list_a = [1,2,3,4,5,6]
a.sumOddLengthSubarrays(list_a)