// 280. 摆动排序
// https://leetcode-cn.com/problems/wiggle-sort/

public void wiggleSort(int[] nums) {
        boolean less = true;
        for (int i = 0; i < nums.length-1; i++) {
            if (less) {
                if (nums[i] > nums[i+1]) {
                    int tmp = nums[i+1];
                    nums[i+1] = nums[i];
                    nums[i] = tmp;
                }
            } else {
                if (nums[i] < nums[i+1]) {
                    int tmp = nums[i+1];
                    nums[i+1] = nums[i];
                    nums[i] = tmp;
                }
            }
            less = !less;
        }
//        System.out.println(nums);
    }