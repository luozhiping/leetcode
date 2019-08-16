// 487. 最大连续1的个数 II
// https://leetcode-cn.com/problems/max-consecutive-ones-ii

public class MaxConsecutiveOnesII {
    public int findMaxConsecutiveOnes(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int dp0 = 0;
        int dp1 = 1;
        int res = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                dp0 += 1;
                dp1 += 1;
            } else {
                dp1 = dp0 + 1;
                dp0 = 0;
            }
            res = Math.max(dp1, Math.max(res, dp0));
        }
        return res;
    }

    public static void main(String[] args) {
        MaxConsecutiveOnesII solution = new MaxConsecutiveOnesII();
        int[] test = {1,0,1,1,0};
        System.out.print(solution.findMaxConsecutiveOnes(test));
    }
}
