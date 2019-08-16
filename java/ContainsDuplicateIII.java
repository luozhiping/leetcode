// 220. 存在重复元素 III
// https://leetcode-cn.com/problems/contains-duplicate-iii/

import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicateIII {
    public long getID(int current, int t) {
        return current < 0 ? (current + 1) / (t+1) - 1 : current / (t+1);
    }


    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (t < 0) return false;
        Map<Long, Long> d = new HashMap<>();
        long w = (long)t + 1;
        for (int i = 0; i < nums.length; ++i) {
            long m = getID(nums[i], t);
            // check if bucket m is empty, each bucket may contain at most one element
            if (d.containsKey(m))
                return true;
            // check the nei***or buckets for almost duplicate
            if (d.containsKey(m - 1) && Math.abs(nums[i] - d.get(m - 1)) < w)
                return true;
            if (d.containsKey(m + 1) && Math.abs(nums[i] - d.get(m + 1)) < w)
                return true;
            // now bucket m is empty and no almost duplicate in nei***or buckets
            d.put(m, (long)nums[i]);
            if (i >= k) d.remove(getID(nums[i - k], t));
        }
        return false;
    }


}
