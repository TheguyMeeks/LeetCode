class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                result.append(number)
                if len(result) == k:
                    return result