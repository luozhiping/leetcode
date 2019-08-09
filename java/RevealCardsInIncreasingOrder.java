// 950. 按递增顺序显示卡牌
// https://leetcode-cn.com/problems/reveal-cards-in-increasing-order/
import java.util.Arrays;
import java.util.LinkedList;

public class RevealCardsInIncreasingOrder {
    public int[] deckRevealedIncreasing(int[] deck) {
        if (deck == null || deck.length == 0) {
            return deck;
        }
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < deck.length; i++) {
            list.add(i);
        }
        Arrays.sort(deck);
        int[] result = new int[list.size()];
        for (int num: deck) {
            result[list.pop()] = num;
            if (list.size() > 0) {
                list.add(list.pop());
            }
        }
        System.out.println(result.toString());
        return result;
    }

    public static void main(String[] args) {
        RevealCardsInIncreasingOrder s = new RevealCardsInIncreasingOrder();
        int[] test = {17,13,11,2,3,5,7};
        int[] result = {2,13,3,11,5,17,7};
        assert s.deckRevealedIncreasing(test).equals(result);
    }
}
