class Solution:
    def minMoves(self, nums: List[int]) -> int:
        big = max(nums)
        count = 0
        for num in nums:
            count += big-num
        return count