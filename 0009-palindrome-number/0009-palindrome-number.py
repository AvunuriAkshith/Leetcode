class Solution:
    def isPalindrome(self, x: int) -> bool:
        var = str(x)
        i = 0
        j = len(var)-1
        while i<j:
            if var[i] != var[j]:
                return False
            i+=1
            j-=1
        return True