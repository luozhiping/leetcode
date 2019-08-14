import java.util.*;
// 187. 重复的DNA序列
// https://leetcode-cn.com/problems/repeated-dna-sequences
public class RepeatedDnaSequences {
    public List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> save = new HashSet<>();
        HashSet<String> result = new HashSet<>();
        List<String> returnList = new ArrayList<>();
        for (int i = 10; i <= s.length(); i++) {
            String current = s.substring(i - 10, i);
            if (save.contains(current)) {
                if (result.add(current)) {
                    returnList.add(current);
                }
            } else {
                save.add(current);
            }
        }

        return returnList;
    }

    public static void main(String[] args) {
        RepeatedDnaSequences solution = new RepeatedDnaSequences();
        String test = "AAAAAAAAAAAA";
        solution.findRepeatedDnaSequences(test);
    }
}
