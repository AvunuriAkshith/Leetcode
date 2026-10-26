class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            seen = set()

            j = i + 1
            while j < n:
                complement = target - nums[j]

                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    # Skip duplicates for the third element
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return result