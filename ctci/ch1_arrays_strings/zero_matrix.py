#!/usr/bin/env python3

import numpy as np

def zero_matrix(mat):
    """ Given an (n,m) matrix, if an element is 0, set the entire row and col to 0.

    Approach: We can do this naively and in-place, however we cannot greedily modify the matrix, since we will lose track of
    where the original 0's lie, and eventually the whole matrix would be filled with 0. Instead we can just track which rows
    and columns need modifying and at the very end, do the modifications. """

    rowsToModify = []
    colsToModify = []

    n, m = mat.shape
    for r in range(n):
        for c in range(m):
            if mat[r, c] == 0:
                rowsToModify.append(r)
                colsToModify.append(c)

    # If numpy is not allowed, simpy iterate through `m` columns
    # for c in range(m):
    #   mat[r, c] = 0
    for r in rowsToModify:
        mat[r, :] = 0
    for c in colsToModify:
        mat[:, c] = 0

