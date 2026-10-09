class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s if char.isalnum())
        str1 = clean_text.lower()
        i = 0
        j = len(str1)-1
        count = 0
        while(i<j):
            if str1[i] != str1[j]:
                return False
                break
            i+=1
            j-=1
        return True