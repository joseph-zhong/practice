#!/usr/bin/env python3
""" 1.8 Zero Matrix """

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

# Optimization: Rather than using O(n + m) space to track the rows and columns needed to modify, we can use the first row
# and column to track our necessary row and column modifications and modify the first row and column if necessary last.
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Flag to check whether to it's necessary to modify our first column.
        set_header_to_zero = False
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            if matrix[r][0] == 0:
                set_header_to_zero = True

            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # If the first column in the first row had a zero, then the whole row must be changed.
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0

        # If any value in the first column had a zero, the whole column must be changed.
        if set_header_to_zero:
            for r in range(rows):
                matrix[r][0] = 0

s = Solution()
mat = [[1,1,1], [1,0,1], [1,1,1]]
s.setZeroes(mat)
print(mat == [[1,0,1],[0,0,0],[1,0,1]])

