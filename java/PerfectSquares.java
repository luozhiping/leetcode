import java.util.HashSet;
import java.util.LinkedList;
// 279. 完全平方数
// https://leetcode-cn.com/problems/perfect-squares/
public class PerfectSquares {
    public int numSquares(int n) {
        LinkedList<Integer> queue = new LinkedList<>();
        HashSet<Integer> handled = new HashSet<>();
        queue.add(n);
        int result = 0;
        while (queue.size() > 0) {

            LinkedList<Integer> tmp = new LinkedList<>();
            result++;
            while (queue.size() > 0) {
                Integer current = queue.pollFirst();
                int t = 1;
                int now = current - t * t;
                while (now >= 0) {
                    if (handled.contains(now)) {
                    } else {
                        tmp.add(now);
                        handled.add(now);
                    }
                    t++;
                    now = current - t * t;
                }
                if (tmp.peekLast() == 0) {
                    return result;
                }
            }
            queue = tmp;
        }
        return -1;
    }

    public static void main(String[] args) {
        PerfectSquares solution = new PerfectSquares();
        assert solution.numSquares(12) == 3;
        assert solution.numSquares(13) == 2;

    }
}
