import java.util.ArrayList;
// 456. 132模式
// https://leetcode-cn.com/problems/132-pattern/
public class Pattern132 {
    public boolean find132pattern(int[] nums) {
        ArrayList<int[]> stack = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (stack.size() == 0 || nums[i] < stack.get(stack.size() - 1)[0]) {
                stack.add(new int[]{nums[i], nums[i]});
            } else {
                int topMin = stack.get(stack.size() - 1)[0];
                while (stack.size() > 0 && nums[i] > stack.get(stack.size() - 1)[1]) {
                    stack.remove(stack.size() - 1);
                }
                if (stack.size() > 0 && nums[i] > stack.get(stack.size() - 1)[0] && nums[i] < stack.get(stack.size() - 1)[1]) {
                    return true;
                }
                stack.add(new int[]{topMin, nums[i]});
            }
        }


        return false;
    }

    public static void main(String[] args) {
        Pattern132 solution = new Pattern132();
        assert solution.find132pattern(new int[]{3, 1, 4, 2});
    }
}
