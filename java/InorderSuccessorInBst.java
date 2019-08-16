// 285. 二叉搜索树中的顺序后继
// https://leetcode-cn.com/problems/inorder-successor-in-bst/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (p.val == root.val) {
            return getFirstInorder(root.right);
        } else if (p.val < root.val) {
            TreeNode result = inorderSuccessor(root.left, p);
            if (result == null) {
                return root;
            } else {
                return result;
            }
        } else {
            return inorderSuccessor(root.right, p);
        }
    }

    public TreeNode getFirstInorder(TreeNode root) {
        if (root == null) {
            return null;
        }
        if (root.left == null) {
            return root;
        } else {
            return getFirstInorder(root.left);
        }
    }
}