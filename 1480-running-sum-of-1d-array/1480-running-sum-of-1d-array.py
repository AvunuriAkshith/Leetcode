class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        i = 0
        sum = nums[i]
        li = []
        li.append(sum)
        while(i<len(nums)-1):
            sum +=nums[i+1]
            li.append(sum)
            i+=1
        return li