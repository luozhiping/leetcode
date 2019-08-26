import java.util.Arrays;
// 416. 分割等和子集
// https://leetcode-cn.com/problems/partition-equal-subset-sum
public class PartitionEqualSubsetSum {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if ((sum & 0x01) == 1) {
            return false;
        }
//        for (int i = 0; i < nums.length; i++) {
        boolean result = findSeq(nums, nums.length - 2, nums[nums.length - 1], sum/2);

//        }
        return result;
    }

    public boolean findSeq(int[] nums, int startIndex, int current, int target) {
        if (startIndex < 0) {
            return current == target;
        }
        if (current == target) {
            return true;
        }
        if (current > target) {
            return false;
        }
        for (int i = startIndex; i >= 0; i--) {
            boolean result = findSeq(nums, i-1, current + nums[i], target);
            if (result) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        PartitionEqualSubsetSum solution = new PartitionEqualSubsetSum();
//        int[] test = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100};
        int[] test = {1, 3, 4, 4};
        assert !solution.canPartition(test);
    }
}
