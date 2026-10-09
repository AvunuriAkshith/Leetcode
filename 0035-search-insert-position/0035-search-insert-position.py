class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                nums.insert(i,target)
                return i
                break
        return length
            