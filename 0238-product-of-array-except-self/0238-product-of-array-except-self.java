import java.util.Arrays;
class Solution {
    public int[] productExceptSelf(int[] nums) {
         // in java specifying the length means all values are 0 by default
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1); // fill with ones instead

        // in this version each iteration will recieve the right prefix to calculate with, then will update the prefix for the next iteration
        int prefix = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] *= prefix;
            prefix *= nums[i];
        }

        int suffix = 1;
        for (int j = nums.length - 1; j >= 0; j--) {
            answer[j] *= suffix;
            suffix *= nums[j];
        }

        return answer;
    }
}