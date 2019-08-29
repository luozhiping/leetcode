import java.util.ArrayList;
import java.util.List;
// 320. 列举单词的全部缩写
// https://leetcode-cn.com/problems/generalized-abbreviation/
public class GeneralizedAbbreviation {
    public List<String> generateAbbreviations(String word) {
        List<String> result = new ArrayList<>();
//        result.add(word);
        result.addAll(doSubString("", word));

        for (String r: result) {
            System.out.print(r + ",");
        }
        return result;
    }

    public List<String> doSubString(String prefix, String word) {
        List<String> result = new ArrayList<>();
        result.add(prefix + word);
        for (int i = 1; i < word.length(); i++) {
            for (int j = 0; j < word.length() - (i-1); j++) {
                if (j+i >= word.length()) {
//                    System.out.println(word+","+ i+","+j);
                    result.add(prefix + word.substring(0,j) + i);
                } else {
                    result.addAll(doSubString(prefix + word.substring(0,j) + i + word.substring(j+i, j+i+1), word.substring(j+i+1)));
                }
            }
        }
        if (word.length() > 0) {
            result.add(prefix + word.length());
        }
        return result;
    }

    public static void main(String[] args) {
        GeneralizedAbbreviation solution = new GeneralizedAbbreviation();
        solution.generateAbbreviations("word");
    }
}
