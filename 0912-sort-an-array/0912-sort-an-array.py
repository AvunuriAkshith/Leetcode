class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <=1:
            return nums
        self._merge_sort(nums, 0, len(nums) - 1)
        return nums
    def _merge_sort(self,nums:list[int], left: int,right:int) -> None:
        if left>=right:
            return
        mid = (left+right)//2
        self._merge_sort(nums,left,mid)
        self._merge_sort(nums,mid+1,right)
        self._merge(nums,left,mid,right)
    def _merge(self,nums:list[int], left:int ,mid:int, right:int)->None:
        temp = []
        i,j = left,mid+1
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
        while i<= mid:
            temp.append(nums[i])
            i+=1
        while j<=right:
            temp.append(nums[j])
            j+=1
        for p in range(len(temp)):
            nums[left+p] = temp[p]
