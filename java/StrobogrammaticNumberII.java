import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
// 247. 中心对称数 II
// https://leetcode-cn.com/problems/strobogrammatic-number-ii/
public class StrobogrammaticNumberII {
    int[] middle = {1, 8}; //0?
    int[] leftRight = {6, 9};
    public List<String> findStrobogrammatic(int n) {
        List<String> result = new ArrayList<>();

        if (n % 2 == 1) {
            for (int m: middle) {
                result.addAll(find(new StringBuilder(String.valueOf(m)), n-1));
            }
            result.addAll(find(new StringBuilder("0"), n-1));
        } else {
            for (int m: middle) {
                result.addAll(find(new StringBuilder(String.valueOf(m) + m), n-2));
            }
            result.addAll(find(new StringBuilder(String.valueOf(leftRight[0])+leftRight[1]), n - 2));
            result.addAll(find(new StringBuilder(String.valueOf(leftRight[1])+leftRight[0]), n - 2));
            if (n > 2) {
                result.addAll(find(new StringBuilder("00"), n-2));
            }
        }
        Collections.sort(result);
        return result;
    }

    public List<String> find(StringBuilder builder, int n) {
        List<String> result = new ArrayList<>();
        if (n == 0) {
            result.add(builder.toString());
            return result;
        }
        for (int m: middle) {
            builder.insert(0, m);
            builder.append(m);
            result.addAll(find(builder, n - 2));
            builder.deleteCharAt(0);
            builder.deleteCharAt(builder.length() - 1);
        }
        builder.insert(0, leftRight[0]);
        builder.append(leftRight[1]);
        result.addAll(find(builder, n - 2));
        builder.deleteCharAt(0);
        builder.deleteCharAt(builder.length() - 1);
        builder.insert(0, leftRight[1]);
        builder.append(leftRight[0]);
        result.addAll(find(builder, n - 2));
        builder.deleteCharAt(0);
        builder.deleteCharAt(builder.length() - 1);
        if (n > 2) {
            builder.insert(0, 0);
            builder.append(0);
            result.addAll(find(builder, n-2));
            builder.deleteCharAt(0);
            builder.deleteCharAt(builder.length() - 1);
        }
        return result;
    }

    public static void main(String[] args) {
        StrobogrammaticNumberII solution = new StrobogrammaticNumberII();
        solution.findStrobogrammatic(2);
    }
}
