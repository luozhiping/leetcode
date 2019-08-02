# 792. 匹配子序列的单词数
# https://leetcode-cn.com/problems/number-of-matching-subsequences/
import java.util.HashMap;

class Solution792 {
    public int numMatchingSubseq(String S, String[] words) {
        System.out.println(words);
        HashMap<String, Integer> finded = new HashMap<String, Integer>();
        int result = 0;
        for (String word: words) {
            if (finded.containsKey(word)) {
                result += 1;
                continue;
            }

            int index1 = 0, index2 = 0;
            while (index1 < S.length() && index2 < word.length()) {
                if (word.charAt(index2) == S.charAt(index1)) index2 ++;
                index1 ++;
            }
            if (index2 == word.length()) {
                result += 1;
                finded.put(word, 1);
            }

        }
        return result;
    }
}









public class NumberOfMatchingSubsequences {
    public static void main( String[] args) {
        Solution792 solution792 = new Solution792();
        String[] words = {"a", "bb", "acd", "ace"};
        System.out.println(solution792.numMatchingSubseq("abcde",words));
    }
}
