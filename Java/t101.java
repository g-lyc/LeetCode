package app;

/**
 * Author:lyc
 */

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
    public boolean isSymmetric(TreeNode root) {

        if (root == null){
            return true;
        }else {
            return checkSame(root.left, root.right);
        }
    }

    private boolean checkSame(TreeNode left, TreeNode right){

        if(left != null && right != null && left.val == right.val){
            return checkSame(left.left, right.right) && checkSame(left.right, right.left);
        }
        else if(left == null && right == null){
            return true;
        }
        else {
            return false;
        }
    }
}

public class t101 {

    public static void main(String[] args) {

        TreeNode p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(2);
        p.left.left = new TreeNode(3);
        p.right.right = new TreeNode(3);
        p.left.right = new TreeNode(4);
        p.right.left = new TreeNode(4);

        Solution result = new Solution();
        boolean res = result.isSymmetric(p);
        System.out.println(res);

    }
}
