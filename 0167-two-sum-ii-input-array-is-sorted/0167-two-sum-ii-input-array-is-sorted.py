class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # remember the first item in the array is 1 not 0, this is an easyyyyy two pointer question

        # all python is done with normal indexing, we just relabel when it's time to report the answer back
        a = 0
        b = len(numbers) - 1

        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a + 1, b + 1] # relabel
            
            if numbers[a] + numbers[b] > target:
                b -= 1

            if numbers[a] + numbers[b] < target:
                a += 1

        return -1

        