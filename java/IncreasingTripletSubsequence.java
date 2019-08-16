// 334. 递增的三元子序列
// https://leetcode-cn.com/problems/increasing-triplet-subsequence/

public class IncreasingTripletSubsequence {

    public boolean increasingTriplet(int[] nums) {
        int dp0 = Integer.MAX_VALUE;
        int dp1 = Integer.MAX_VALUE;
//        int dp2 = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            dp0 = Math.min(dp0, nums[i]);
            if (nums[i] > dp0) {
                dp1 = Math.min(dp1, nums[i]);
            }
            if (nums[i] > dp1) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        IncreasingTripletSubsequence solution = new IncreasingTripletSubsequence();
        int[] test = {1,2,1,1,1};
        System.out.print(solution.increasingTriplet(test));
    }

}
