class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # remember the first item in the array is 1 not 0, this is an easyyyyy two pointer question

        # all python is done with normal indexing, we just relabel when it's time to report the answer back
        a = 0
        b = len(numbers) - 1

        while a < b:
            s = numbers[a] + numbers[b]
            if s == target:
                return [a + 1, b + 1] # relabel
            elif s > target:
                b -= 1
            else:
                a += 1


        