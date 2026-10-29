class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        # fix a number then run two pointers on the rest of the list

        # each number and how many times we've seen it
        output = []

        # for index, num in enumerate(nums):
        #     # if the number was already there before, increase its count by one
        #     # else, initialize its count once
        #     seen[num] = seen.get(num, 0) + 1

        # the number that will be fixed at the start of each while loop run
        fixed = 0
        lt = fixed + 1
        rt = len(nums) - 1

        while fixed < len(nums) - 2:
            # all numbers to the right of the fixed number are at least as big as the fixed number. if the fixed number positive, everything after is a positive number, and we'd essentially be asking our two pointers to find two positive values to add up to a negative fixed number, which is impossible. we can break here instead of continuing, because once we come across that first positive fixed value, everything to it's right is also positive, and will have the problem as this positive fixed value, so there's no point in checking them either
            if nums[fixed] > 0:
                break
            target = -1 * nums[fixed]
            while lt < rt:
                val_l = nums[lt]
                val_r = nums[rt]

                s = val_l + val_r

                # if fixed + val + val = 0 then val + val = -fixed. same as two sum with a target

                if s == target:
                    output.append([nums[fixed], val_l, val_r])
                    lt += 1
                    rt -= 1

                    # skip duplicates while we stay in the window
                    while lt < rt and nums[lt] == val_l:
                        lt += 1
                    while rt > lt and nums[rt] == val_r:
                        rt -= 1
                elif s > target:
                    rt -= 1
                else:
                    lt += 1
            # reset
            fixed += 1
            while fixed < len(nums) - 2 and nums[fixed] == nums[fixed - 1]:
                fixed += 1
            lt = fixed + 1
            rt = len(nums) - 1

        return output








        



        