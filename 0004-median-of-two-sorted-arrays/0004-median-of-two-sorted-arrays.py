class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # came back to revisit this, commenting to solidify understanding because this one was a doozy
        # we use two pointers, both pointing at the start of each of the lists. nums1[i] then nums2[j]
        # since they are both sorted we compare each of their values and take the smaller one, then slide that arrays
        # pointer to the next value because in classic two pointer fashion, once we prove that the index is either useless 
        # or useful we can permanently ditch it and move on

        new_list = []
        i, j = 0, 0

        # k always points at the next EMPTY slot
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        
        # since the main loop stops as soon as one array is empty, we need to handle any possible leftovers
        new_list.extend(nums1[i:])
        new_list.extend(nums2[j:])


        if len(new_list) % 2 == 0:
            right_i = len(new_list) // 2
            left_i = right_i - 1
            result = (new_list[right_i] + new_list[left_i]) / 2.0
            return result
        else:
            return new_list[len(new_list) // 2]


        