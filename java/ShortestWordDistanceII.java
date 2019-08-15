import java.util.ArrayList;
import java.util.HashMap;
// 244. 最短单词距离 II
// https://leetcode-cn.com/problems/shortest-word-distance-ii
public class ShortestWordDistanceII {
    HashMap<String, ArrayList<Integer>> position = new HashMap<>();
    int defaultDistance = 0;
    public ShortestWordDistanceII(String[] words) {
        for (int i = 0; i < words.length; i++) {
            if (position.containsKey(words[i])) {
                position.get(words[i]).add(i);
            } else {
                ArrayList<Integer> l = new ArrayList<>();
                l.add(i);
                position.put(words[i], l);
            }
        }
        defaultDistance = words.length;
    }

    public int shortest(String word1, String word2) {
        ArrayList<Integer> list1 = position.get(word1);
        ArrayList<Integer> list2 = position.get(word2);
        int result = defaultDistance;
        for(int i=0,j=0; i <list1.size() && j<list2.size();) {
            result = Math.min(result, Math.abs(list2.get(j) - list1.get(i)));
            if (list1.get(i) > list2.get(j)) {
                j++;
            } else {
                i++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String[] test = {"practice", "makes", "perfect", "coding", "makes"};
        ShortestWordDistanceII solution = new ShortestWordDistanceII(test);

        assert solution.shortest("makes", "coding") == 1;
        assert solution.shortest("practice", "coding") == 3;

    }
}
