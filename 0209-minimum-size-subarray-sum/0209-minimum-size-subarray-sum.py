class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        c_sum = 0
        for i in range(len(nums)):
            c_sum += nums[i]
            while c_sum>=target:
                min_len = min(min_len, i-left+1)
                c_sum -= nums[left]
                left+=1
        if min_len == float('inf'):
            return 0
        return min_len