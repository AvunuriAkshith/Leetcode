class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        i = 0
        j = len(s)-1

        vov = ['a','e','i', 'o', 'u']

        while i<j:
            if s[i].lower() in vov:
                if s[j].lower() in vov:
                    s[i],s[j] = s[j],s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(s)