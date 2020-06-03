package com.company;

import java.util.ArrayList;
import java.util.List;

/**
 * josephz
 * 2019-03-18
 */

public class A {
    private String a;
    private List<Integer> vals;

    public A() {
        System.out.println("A: constructor STARTED");
        vals = new ArrayList<Integer>();
        a = toString();
        System.out.println("A: constructor FINISHED");
    }

    public void add(int asdf) {
        a = null;
        a = toString();
    }

    @Override
    public String toString() {
        System.out.println("A: toString");
        if (a != null) {
            return a;
        }
        return vals.toString();
    }
}
