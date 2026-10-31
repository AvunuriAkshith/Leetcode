class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        limit = min(len(first), len(last))
        while i<limit and first[i] == last[i]:
            i+=1
        return first[:i]