import java.util.ArrayList;
import java.util.Arrays;
// 846. 一手顺子
// https://leetcode-cn.com/problems/hand-of-straights/
public class HandOfStraights {
    public boolean isNStraightHand(int[] hand, int W) {
        if (hand.length % W != 0) {
            return false;
        }
        Arrays.sort(hand);
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        for (int i = 0; i < hand.length; i++) {
            int cur = hand[i];
            boolean putted = false;
            for (ArrayList<Integer> node: result) {
                if (node.size() < W) {
                    if (node.get(node.size() - 1) == cur) {
                        continue;
                    } else if (node.get(node.size() - 1) + 1 == cur) {
                        node.add(cur);
                        putted = true;
                        break;
                    } else if (node.get(node.size() - 1) + 1 < cur) {
                        return false;
                    }
                }
            }
            if (!putted) {
                ArrayList<Integer> tmp = new ArrayList<>();
                tmp.add(cur);
                result.add(tmp);
            }
        }
        for (ArrayList<Integer> cur: result) {
            if (cur.size() != W) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        HandOfStraights solution = new HandOfStraights();
        int[] hand = {1,2,3,6,2,3,4,7,8};
        System.out.println(solution.isNStraightHand(hand, 3));
    }
}
