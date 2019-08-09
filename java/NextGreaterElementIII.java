// 556. 下一个更大元素 III
// https://leetcode-cn.com/problems/next-greater-element-iii
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class NextGreaterElementIII {
    public int nextGreaterElement(int n) {
        int tmp = n;
        ArrayList<Integer> list = new ArrayList<>();
        boolean findedPos = false;
        int pos = -1;
        int num = tmp % 10;
        list.add(num);
        tmp /= 10;
        while (tmp > 0) {
            num = tmp%10;
            list.add(num);
            if (!findedPos) {
                int tmpPos = -1;
                int tmpMin = Integer.MAX_VALUE;
                for (int i = 0; i < list.size() - 1; i++) {
                    if (list.get(i) > num) {
                        if (list.get(i) == num + 1) {
                            tmpPos = i;
                            break;
                        } else if (list.get(i) < tmpMin){
                            tmpPos = i;
                            tmpMin = list.get(i);
                        }
                    }
                }
                if (tmpPos != -1) {
                    findedPos = true;
                    pos = list.size() - 1;
                    int middle = list.get(tmpPos);
                    list.set(tmpPos, list.get(list.size() - 1));
                    list.set(list.size() - 1, middle);
                }
            }
            tmp /= 10;
        }
        if (!findedPos) {
            return -1;
        }
//        System.out.println(list.toString());
//        System.out.println(pos);
        List<Integer> head = list.subList(0, pos);
        List<Integer> tail = list.subList(pos, list.size());
        Collections.sort(head);
        long result = 0L;
        for (int i = tail.size() - 1; i >= 0; i--) {
            result = result * 10 + tail.get(i);
        }
        for (int i = 0; i < head.size(); i++) {
            result = result * 10 + head.get(i);
        }
//        System.out.println(result);
        if (result > Integer.MAX_VALUE) {
            return -1;
        }
        return (int)result;
    }

    public static void main(String[] args) {
	// write your code here
        System.out.println("hello world");
        NextGreaterElementIII a = new NextGreaterElementIII();
        assert a.nextGreaterElement(1999999999) == -1;
        assert a.nextGreaterElement(123851) == 125138;
        assert(a.nextGreaterElement(65453230) == 65453302);
        assert(a.nextGreaterElement(13296542) == 13422569);
        assert(a.nextGreaterElement(1234) == 1243);
        assert(a.nextGreaterElement(4321) == -1);
        assert(a.nextGreaterElement(12) == 21);
        assert(a.nextGreaterElement(12443322) == 13222344);

    }
}
