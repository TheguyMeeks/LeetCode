class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_s = set(nums)
        count = 1
        best = 0

        for num in nums_s:
            n = num
            if n - 1 in nums_s:
                continue

            while n + 1 in nums_s:
                count += 1
                n += 1

            best = max(count, best)
            count = 1
        
        return best
