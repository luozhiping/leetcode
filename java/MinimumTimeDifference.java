import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
// 539. 最小时间差
// https://leetcode-cn.com/problems/minimum-time-difference/
public class MinimumTimeDifference {
    public int findMinDifference(List<String> timePoints) {
        Collections.sort(timePoints);
        for(String i: timePoints) {
            System.out.println(i);
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < timePoints.size() - 1; i++) {
            result = Math.min(result, getDiff(timePoints.get(i), timePoints.get(i+1)));
        }
        String[] times1 = timePoints.get(0).split(":");
        times1[0] = String.valueOf(Integer.valueOf(times1[0]) + 24);
        result = Math.min(result, getDiff(timePoints.get(timePoints.size() - 1), times1[0] + ":" + times1[1]));
        return result;
    }

    public int getDiff(String time1, String time2) {
        String[] times2 = time2.split(":");
        String[] times1 = time1.split(":");
        return (Integer.valueOf(times2[0]) - Integer.valueOf(times1[0])) * 60 + Integer.valueOf(times2[1]) - Integer.valueOf(times1[1]);
    }

    public static void main(String[] args) {
        MinimumTimeDifference solution = new MinimumTimeDifference();
        List<String> test = new ArrayList<>();
        test.add("00:00");
        test.add("10:08");
        test.add("05:05");
        solution.findMinDifference(test);

    }
}
