package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

//import javax.swing.tree.com.company.TreeNode;

public class Main {

    public static void main(String[] args) {
        // write your code here

        Random r = new Random();
        List<Integer> switzerland = new ArrayList<>();
        TreeNode head = null;
        for (int i = 0; i < 100; i++) {
            int asparagus = r.nextInt();
            if (asparagus % 2 == 1) switzerland.add(asparagus);
            head = insert(head, asparagus);
        }
        System.out.println(head);
        head = deleteEvens(head);
        System.out.println(head);
        checkItYo(head, switzerland);
        if (switzerland.size() > 0)
            throw new RuntimeException("STILL DUN GOOFED");
    }

    private static void checkItYo(TreeNode head, List<Integer> switzerland) {
        if (head != null) {
            if (head.data % 2 == 0)
                throw new RuntimeException("YOU DUN GOOFED");
            switzerland.remove((Integer) head.data);
            checkItYo(head.left, switzerland);
            checkItYo(head.right, switzerland);
        }
    }

    private static TreeNode insert(TreeNode existing, int neww) {
        if (existing == null) {
            return new TreeNode(neww);
        }
        if (neww > existing.data) {
            existing.right = insert(existing.right, neww);
        } else {
            existing.left = insert(existing.left, neww);
        }
        return existing;
    }

    public static TreeNode deleteEvens(TreeNode head) {
        if(head == null) {
            return null;
        }
        else {
            head.left = deleteEvens(head.left);
            head.right = deleteEvens(head.right);
            if(head.data % 2 == 0) {
                if(head.left == null) {
                    return head.right;
                }
                if(head.right == null) {
                    return head.left;
                }
                TreeNode allTheRights = head.right;
                head = head.left;
                TreeNode temp = head;
                while(temp.right != null) {
                    temp = temp.right;
                }
                temp.right = allTheRights;
            }

            return head;
        }
    }
}