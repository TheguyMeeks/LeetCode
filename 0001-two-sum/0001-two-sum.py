class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {} 

        for index, num in enumerate(nums):
            complement = target - num

            if complement in pairs:
                return [index, pairs[complement]]
            
            pairs[num] = index


