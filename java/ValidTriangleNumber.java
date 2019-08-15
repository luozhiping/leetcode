import java.util.Arrays;
import java.util.Random;

// 611. 有效三角形的个数
// https://leetcode-cn.com/problems/valid-triangle-number/
public class ValidTriangleNumber {

    public int triangleNumber2(int[] nums) {
        int result = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i+1; j < nums.length - 1; j++) {
                int now = nums[i] + nums[j];
                for (int n = j+1; n < nums.length; n++) {
                    if (nums[n] == 0) continue;
                    if (now > nums[n]) {
                        result++;
                    } else {
                        break;
                    }
                }
            }
        }
        return result;
    }

    public int triangleNumber(int[] nums) {
        int result = 0;
        Arrays.sort(nums);
        for (int i = nums.length - 1; i >= 2; i--) {
            int a = 0;
            int b = i - 1;
            while (a < b) {
                if (nums[a] + nums[b] > nums[i]) {
                    result += (b-a);
                    b--;
                } else {
                    a++;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        ValidTriangleNumber solution = new ValidTriangleNumber();
        int[] test = {2, 2, 3, 4};
        System.out.println(solution.triangleNumber(test));

        Random random = new Random();
        int[] test2 = new int[random.nextInt(1000)];
        for (int i = 0; i < test2.length; i++) {
            test2[i] = random.nextInt(1000);
            System.out.print(test2[i] + ",");
        }

        System.out.println(solution.triangleNumber(test2));
    }
}
