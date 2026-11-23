class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {} # number : it's index

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in pairs:
                return [idx, pairs[complement]]
            
            pairs[num] = idx
