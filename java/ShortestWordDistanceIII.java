import java.util.ArrayList;
import java.util.HashMap;
// 245. 最短单词距离 III
// https://leetcode-cn.com/problems/shortest-word-distance-iii/
public class ShortestWordDistanceIII {
    public ShortestWordDistanceIII(String[] words) {

    }

    public int shortestWordDistance(String[] words, String word1, String word2) {
        ArrayList<Integer> l1 = new ArrayList<>();
        ArrayList<Integer> l2 = new ArrayList<>();

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                l1.add(i);
            } else if (words[i].equals(word2)) {
                l2.add(i);
            }
        }
        int result = words.length;
        if (!word1.equals(word2)) {
            for(int i=0,j=0; i <l1.size() && j<l2.size();) {
                result = Math.min(result, Math.abs(l2.get(j) - l1.get(i)));
                if (l1.get(i) > l2.get(j)) {
                    j++;
                } else {
                    i++;
                }
            }
        } else {
            for (int i = 1; i < l1.size(); i++) {
                result = Math.min(result, Math.abs(l1.get(i) - l1.get(i-1)));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String[] test = {"practice", "makes", "perfect", "coding", "makes"};
        ShortestWordDistanceIII solution = new ShortestWordDistanceIII(test);

        assert solution.shortestWordDistance(test,"makes", "coding") == 1;
        assert solution.shortestWordDistance(test,"practice", "coding") == 3;
        assert solution.shortestWordDistance(test,"makes", "makes") == 3;

    }
}
