// 984. 不含 AAA 或 BBB 的字符串
// https://leetcode-cn.com/problems/string-without-aaa-or-bbb/
public class StringWithoutAaaOrBbb {
    public String strWithout3a3b(int A, int B) {
        StringBuilder result=  new StringBuilder();
        if (A == B) {
            result.append("a");
            A--;
        }
        while (A > 0 || B > 0) {
            if (A > B) {
                if (A - B > 1) {
                    result.append("aa");
                    A -= 2;
                } else {
                    result.append("a");
                    A -= 1;
                }
                if (B > 0) {
                    result.append("b");
                    B--;
                }
            } else if (B > A) {
                if (B - A > 1) {
                    result.append("bb");
                    B -= 2;
                } else {
                    result.append("b");
                    B -= 1;
                }
                if (A > 0) {
                    result.append("a");
                    A--;
                }
            }
        }
        System.out.println(result.toString());
        return result.toString();
    }

    public static void main(String[] args) {
        StringWithoutAaaOrBbb solution = new StringWithoutAaaOrBbb();
        solution.strWithout3a3b(1, 2).equals("abb");
        solution.strWithout3a3b(4, 1).equals("aabaa");
        solution.strWithout3a3b(3, 3).equals("aabaa");

    }
}
