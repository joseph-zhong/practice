package com.company; /**
 * Created by Joseph on 11/3/15.
 */

/**
 * Joseph
 * 11/3/15
 * CSE 143X
 * TA: Emerson Matson
 * HW: ...
 * <p>
 * This class will...
 */
public class TreeNode {
    public TreeNode left;
    public TreeNode right;

    public int data;

    public TreeNode() {
        this(null, null, 0);
    }

    public TreeNode(int data) {
        this(null, null, data);
    }

    public TreeNode(TreeNode left, TreeNode right, int data) {
        this.left = left;
        this.right = right;
        this.data = data;
    }

    @Override
    public String toString() {
        StringBuilder x = new StringBuilder();
        if(left != null) x.append("[" + left + "] ");
        x.append(data);
        if(right != null) x.append(" [" + right + "]");
        return x.toString();
    }
}
