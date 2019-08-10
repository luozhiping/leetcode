// 1101. 彼此熟识的最早时间
// https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

public class TheEarliestMomentWhenEveryoneBecomeFriends {

    public int earliestAcq(int[][] logs, int N) {
        Arrays.sort(logs, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        ArrayList<LinkedList<Integer>> arrayList = new ArrayList<>();
        for (int i = 0; i < N; i++ ) {
            LinkedList<Integer> list = new LinkedList<>();
            list.add(i);
            arrayList.add(list);
        }
        for (int i = 0; i < logs.length; i++) {
            int aIndex = -1;
            int bIndex = -1;
            int a = logs[i][1];
            int b = logs[i][2];
            for (int j = 0; j < arrayList.size(); j++) {
                LinkedList<Integer> list = arrayList.get(j);
                if (aIndex == -1 && list.indexOf(a) != -1) {
                    aIndex = j;
                }
                if (bIndex == -1 && list.indexOf(b) != -1) {
                    bIndex = j;
                }
                if (aIndex != -1 && bIndex != -1) {
                    break;
                }
            }
            if (aIndex != bIndex) {
                LinkedList<Integer> bb = arrayList.get(bIndex);
                LinkedList<Integer> aa = arrayList.get(aIndex);
                arrayList.remove(bb);
                aa.addAll(bb);

                if (arrayList.size() == 1) {
                    return logs[i][0];
                }
            }
        }


        return -1;
    }


    public static void main(String[] args) {
        System.out.println("Hello World!");
        TheEarliestMomentWhenEveryoneBecomeFriends solution = new TheEarliestMomentWhenEveryoneBecomeFriends();
        int[][] test = {{20190101, 0, 1}, {20190104, 3, 4}, {20190107, 2, 3}, {20190211, 1, 5}, {20190224, 2, 4}, {20190330, 0, 3}, {20190312, 1, 2}, {20190322, 4, 5}};
        assert solution.earliestAcq(test, 6) == 20190330;
    }
}
