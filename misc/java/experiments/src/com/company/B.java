package com.company;

import java.util.Objects;

/**
 * josephz
 * 2019-03-18
 */

public class B extends A {


    private int prod;

    public B() {
        super();
        System.out.println("B: constructor STARTED");
        prod = 1;
        System.out.println("B: constructor FINISHED");
    }

    @Override
    public String toString() {
        System.out.println("B: toString");
        return super.toString();
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
//        if (o == null || getClass() != o.getClass()) return false;
        if (!(o instanceof B)) return false;
        B b = (B) o;
        return prod == b.prod;
    }

    @Override
    public int hashCode() {
        return Objects.hash(prod);
    }
}
