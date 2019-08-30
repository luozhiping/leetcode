import java.util.ArrayList;
import java.util.List;
// 216. 组合总和 III
// https://leetcode-cn.com/problems/combination-sum-iii/
public class CombinationSumIII {
    public List<List<Integer>> combinationSum3(int k, int n) {

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 1; i <= 9; i++ ) {
            List<Integer> now = new ArrayList<>(k);
            now.add(i);
            if (now.size() == k) {
                if (i == n) {
                    result.add(now);
                    break;
                }
            } else {
                List<List<Integer>> tmp = dp(now, i, k, n);
                if (tmp != null) {
                    result.addAll(tmp);
                }
            }
        }
        return result;
    }

    public List<List<Integer>> dp(List<Integer> seq, int sum, int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        if (sum > n) {
            return result;
        }
        List<Integer> cur = new ArrayList<>(seq);
        if (seq.size() == k - 1) {
            if (n - sum > seq.get(seq.size() - 1) && n - sum <= 9) {
                cur.add(n - sum);
                result.add(cur);
            } else {
                return result;
            }
        } else {
            for (int i = seq.get(seq.size() - 1) + 1; i <= 9; i++) {
                if (sum + i > n) {
                    break;
                }
                cur.add(i);
                List<List<Integer>> tmp = dp(cur, sum+i, k, n);
                result.addAll(tmp);
                cur.remove(cur.size()-1);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        CombinationSumIII solution = new CombinationSumIII();
        solution.combinationSum3(3, 9);
    }
}
