class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = list(stones)
        while len(stones)>1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if y!=x:
                stones.append(y-x)
        return stones[0] if stones else 0