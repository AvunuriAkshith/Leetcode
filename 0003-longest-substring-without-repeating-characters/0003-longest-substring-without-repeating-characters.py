class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[i])
            current_len = i-left+1
            max_len = max(max_len,current_len)
        return(max_len)

            