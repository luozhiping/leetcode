// 186. 翻转字符串里的单词 II
// https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/
public class ReverseWordsInAStringII {
    public void reverseWords(char[] s) {
        int start = 0;
        int end = 0;
        for (int i = 0; i < s.length; i++) {
            if (s[i] != ' ') {
                end++;
            } else {
                reverse(s, start, end-1);
                start = i + 1;
                end = i + 1;
            }
        }
        reverse(s, start, end-1);
        reverse(s, 0 ,s.length-1);
//        for (char c: s) {
//            System.out.print(c);
//        }
    }

    public void reverse(char[] s, int start, int end) {
        while (start < end) {
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        ReverseWordsInAStringII solution = new ReverseWordsInAStringII();
        char[] test = {'t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'};
        solution.reverseWords(test);
    }
}
