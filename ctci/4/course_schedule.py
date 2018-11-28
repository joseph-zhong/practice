#!/usr/bin/env python3
"""
https://leetcode.com/problems/course-schedule/
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Count number of prereqs for topological sorting.
        ins = [0 for _ in range(numCourses)]
        for (course, prereq) in prerequisites:
            ins[course] += 1

        # Prepare BFS search across topologically sorted vertices.
        queue = []
        for course in range(numCourses):
            if ins[course] == 0:
                queue.append(course)

        count = len(queue)
        while len(queue) > 0:
            course = queue.pop(0)
            for c, p in prerequisites:
                # BFS Search: If course ticks a prereq,
                # decrement the remaining prereqs for the course `c`.
                if course == p:
                    ins[c] -= 1
                    if ins[c] == 0:
                        # Once prereqs are met, we can take the course.
                        queue.append(c)
                        count += 1
        return count == numCourses

