// 378. 有序矩阵中第K小的元素
// https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
public class KthSmallestElementInASortedMatrix {
    public int kthSmallest(int[][] matrix, int k) {
        int left = matrix[0][0];
        int right = matrix[matrix.length-1][matrix[0].length-1];
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = countLess(matrix, mid);
            if (count < k) {
                left = mid+1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public int countLess(int[][] matrix, int target) {
        int n = matrix.length;
        int i = n-1;
        int j = 0;
        int result = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= target) {
                result += i+1;
                ++j;
            } else {
                --i;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        KthSmallestElementInASortedMatrix solution = new KthSmallestElementInASortedMatrix();
        int[][] test = {{1, 2}, {1, 3}};
        solution.kthSmallest(test, 3);
    }
}
