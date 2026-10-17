class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        pairs = [("CM", 900), ("CD", 400), ("XC", 90),
                 ("XL", 40), ("IX", 9), ("IV", 4)]
        for pair,value in pairs:
            if pair in s:
                result+=value
                s = s.replace(pair, "")
        values = {"M": 1000, "D": 500, "C": 100, "L": 50,
                  "X": 10, "V": 5, "I": 1}
        for c in s:
            result += values[c]
        return result