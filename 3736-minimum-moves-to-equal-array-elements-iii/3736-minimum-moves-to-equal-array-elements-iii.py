class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        big = nums[-1]
        count = 0
        for i in range(len(nums)-1):
            while(nums[i]!=big):
                nums[i]+=1
                count+=1
        return count