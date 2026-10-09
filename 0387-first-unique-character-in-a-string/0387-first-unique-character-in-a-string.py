class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for key,value in enumerate(s):
            if dic[value] == 1:
                return key
        return -1
