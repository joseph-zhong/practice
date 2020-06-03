#!/usr/bin/env python3
""" 4.7 Build Order """

def validBuildOrder(projs, deps):
    """ Prints a valid build order given a list of projects and dependencies.
    :param projs: List[int]
    :param deps: Tuple[int a, int b] representing `a` must be built before `b`.

    Approach: Dependency graphs can be represented with topological sorting, and whether or not a valid build order
    exists can be computed by traversing the topologically sorted graph from start to finish without cycles.
    """
    queue = []
    seen = set()

    # Build in-vertex counts for topo sort.
    ins = [0 for _ in range(len(projs))]
    for a, b in deps:
        ins[b] += 1
    for proj in range(len(ins)):
        if ins[proj] == 0:
            queue.append(proj)

    res = []
    while len(queue) > 0:
        proj = queue.pop(0)
        if proj in seen:
            return []
        seen.add(proj)
        res.append(proj)

        for a, b in deps:
            if proj == a:
                ins[b] -= 1
                if ins[b] == 0:
                    queue.append(b)
    return res

print(validBuildOrder(
    projs=(0,1,2,3),
    deps=((0, 1), (1, 2), (1, 3))
    ))

