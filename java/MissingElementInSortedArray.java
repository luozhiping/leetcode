// 1060. 有序数组中的缺失元素
// https://leetcode-cn.com/problems/missing-element-in-sorted-array/
public class MissingElementInSortedArray {
    public int missingElement(int[] nums, int k) {
        int start = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - start - 1 < k) {
                k -= (nums[i] - start - 1);
                start = nums[i];
            } else {
                return start + k;
            }
        }
        return start + k;
    }

    public static void main(String[] args) {
        MissingElementInSortedArray solution = new MissingElementInSortedArray();
        int[] test = {4,7,9,10};
        assert solution.missingElement(test, 1) == 5;
        int[] test2 = {4,7,9,10};
        assert solution.missingElement(test2, 3) == 8;
        int[] test3 = {1, 2, 4};
        assert solution.missingElement(test3, 3) == 6;
    }
}
