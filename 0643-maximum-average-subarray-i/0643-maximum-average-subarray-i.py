class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        s = 0
        ans = []
        while right<len(nums):
            s+=nums[right]
            if right-left+1 == k:
                avg = s/k
                ans.append(avg)
                s-=nums[left]
                left+=1
            right+=1
        return max(ans)