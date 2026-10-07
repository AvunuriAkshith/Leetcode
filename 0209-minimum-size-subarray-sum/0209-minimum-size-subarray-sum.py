class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        min_len = float('inf')
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                length = r-l+1
                min_len = length if length<min_len else min_len

                s-=nums[l]
                l+=1
            r+=1
        if min_len == float('inf'):
            return 0
        return min_len