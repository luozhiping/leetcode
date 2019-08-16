// 376. 摆动序列
// https://leetcode-cn.com/problems/wiggle-subsequence/

public class WiggleSubsequence {

    public int wiggleMaxLength(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        up[0] = 1;
        down[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                up[i] = down[i - 1] + 1;
                down[i] = down[i - 1];
            } else if (nums[i] < nums[i - 1]) {
                down[i] = up[i - 1] + 1;
                up[i] = up[i - 1];
            } else {
                up[i] = up[i - 1];
                down[i] = down[i - 1];
            }

        }
        return Math.max(up[nums.length - 1], down[nums.length - 1]);
    }

    public static void main(String[] args) {
        WiggleSubsequence solution = new WiggleSubsequence();
        int[] test = {1, 7, 4, 9, 2, 5};
        assert solution.wiggleMaxLength(test) == 6;
        int[] test2 = {1, 17, 5, 10, 13, 15, 10, 5, 16, 8};
        assert solution.wiggleMaxLength(test2) == 7;
        int[] test3 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        assert solution.wiggleMaxLength(test3) == 2;

    }
}
