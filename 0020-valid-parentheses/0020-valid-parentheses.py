class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_map = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in match_map:
                if not stack or stack.pop() != match_map[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
