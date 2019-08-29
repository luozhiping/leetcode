// 962. 最大宽度坡
// https://leetcode-cn.com/problems/maximum-width-ramp/
public class MaximumWidthRamp {
    public int maxWidthRamp(int[] A) {
        // A[i] >= A[i-1]
        // dp[i] = d
        int result = 0;
        for (int i = 1; i < A.length; i++) {

            for (int j = 0; j < i; j++) {
                if (i-j <= result) {
                    break;
                }
                if (A[j] <= A[i]) {
                    result = Math.max(result, i-j);
                    break;
                }
            }
        }


//        System.out.println(result);
        return result;
    }

    public static void main(String[] args) {
        MaximumWidthRamp solution = new MaximumWidthRamp();
//        int[] test = {6,0,8,2,1,5};
//        assert solution.maxWidthRamp(test) == 4;

        int[] test2 = {9,8,1,0,1,9,4,0,4,1};
        assert solution.maxWidthRamp(test2) == 7;


    }

}
