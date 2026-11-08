class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = []

        for num in range(100, 1000, 2):

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            temp = freq[:]

            temp[a] -= 1
            temp[b] -= 1
            temp[c] -= 1

            if min(temp) >= 0:
                ans.append(num)

        return ans