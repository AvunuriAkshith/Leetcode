class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        i = 0
        stack = []
        for ch in pushed:
            stack.append(ch)
            while i<len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i+=1
        return not stack