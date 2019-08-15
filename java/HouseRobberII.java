import java.util.Random;
// 213. 打家劫舍 II
// https://leetcode-cn.com/problems/house-robber-ii/
public class HouseRobberII {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[2]);
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int result = nums[0];
        for (int i = 2; i < nums.length - 1; i++) {
            int tmp = dp[i - 2];
            if (i > 2) {
                tmp = Math.max(tmp, dp[i - 3]);
            }
            result = Math.max(result, tmp+nums[i]);
            dp[i] = tmp+nums[i];

        }
        result = Math.max(result, dp[dp.length - 2]);


        dp = new int[nums.length];
        dp[1] = nums[1];
        result = Math.max(result, dp[1]);
        for (int i = 3; i < nums.length; i++) {
            int tmp = Math.max(dp[i - 2], dp[i - 3]);
            result = Math.max(result, tmp+nums[i]);
            dp[i] = tmp+nums[i];
        }
        result = Math.max(result, dp[dp.length - 1]);

        dp = new int[nums.length];
        dp[2] = nums[2];
        result = Math.max(result, dp[1]);
        for (int i = 4; i < nums.length; i++) {
            int tmp = Math.max(dp[i - 2], dp[i - 3]);
            result = Math.max(result, tmp+nums[i]);
            dp[i] = tmp+nums[i];
        }
        result = Math.max(result, dp[dp.length - 1]);
//        System.out.print(result);
        return result;
    }

    public static void main(String[] args) {
        HouseRobberII solution = new HouseRobberII();
        int[] test = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5};
        assert solution.rob(test) == 16;
        Random random =new Random();
        int[] test2 = new int[random.nextInt(1000)];
        for (int i = 0; i < test2.length; i++) {
            test2[i] = random.nextInt(1000);
            System.out.print(test2[i]+",");
        }

    }
}
