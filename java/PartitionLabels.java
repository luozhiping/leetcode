import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// 763. 划分字母区间
// https://leetcode-cn.com/problems/partition-labels/
public class PartitionLabels {
    public List<Integer> partitionLabels(String S) {
//        HashMap<String, Integer> start = new HashMap<>();
//        HashMap<String, Integer> end = new HashMap<>();
        int[] start = new int[26];
        int[] end = new int[26];
        for (int i = 0; i < 26; i++) {
            start[i] = -1;
            end[i] = -1;
        }
        for (int i = 0; i < S.length(); i++) {
            int cur = S.charAt(i) - 'a';
            if (start[cur] == -1) {
                start[cur] = i;
            }
            end[cur] = i;
        }
//        for (int i = 0; i < 26; i++) {
//            char key = (char)('a' + i);
//            System.out.println(key + "," + start[i] + "," + end[i]);
//        }

        int startIndex = 0;
        int endIndex = 0;
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < S.length(); i++) {
            int cur = S.charAt(i) - 'a';
            int curStart = start[cur];
            int curEnd = end[cur];
            if (curStart > endIndex) {
//                System.out.println(endIndex - startIndex + 1);
                result.add(endIndex - startIndex + 1);
                startIndex = curStart;
                endIndex = curEnd;
            } else {
                endIndex = Math.max(curEnd, endIndex);
            }
        }
        result.add(endIndex - startIndex + 1);
        return result;
    }

    public static void main(String[] args) {
        PartitionLabels solution = new PartitionLabels();
        solution.partitionLabels("ababcbacadefegdehijhklij");
    }

}
