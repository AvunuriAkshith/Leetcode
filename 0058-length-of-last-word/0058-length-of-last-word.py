class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        max = 0
        for i in range(len(arr)):
            max = len(arr[i])
        return max