class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        # solve for each numbers prefix
        for i in range(len(nums)):
            if i == 0:
                prefix = 1
                answer[i] = prefix
            else:
                prefix = answer[i - 1] * nums[i - 1]
                answer[i] = prefix

        # solve for each numbers suffix, then join that product with the prefix already sitting in the curresponding index
        # we need an extra tracking variable this time, because unlike the prefix loop, the answer list 
        # is not holding suffix[j + 1], like it was holding prefix[i - 1]. Each time j moves, everything to the right of j
        # is a finished answer, and everything to the left is a prefix waiting for a suffix to be multiplied to it
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix = 1
                answer[j] = answer[j] * suffix
            else:
                suffix = suffix * nums[j + 1]
                answer[j] *= suffix
        
        return answer