package app;

public class t100 {
    public static void main(String[] args) {
        Solution result = new Solution();

        // 创建两个二叉树
        TreeNode p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(3);

        TreeNode q = new TreeNode(1);
        q.left = new TreeNode(2);
        q.right = new TreeNode(3);

        boolean res = result.isSameTree(p,q);
        System.out.println(res);
    }
}

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null) {
            return false;
        }

        return p.val==q.val&&isSameTree(p.right,q.right)&&isSameTree(p.left,q.left);

    }
}

