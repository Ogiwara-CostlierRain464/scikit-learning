from typing import Union, Tuple, List
from algorithm_introduction.helper import *

price_table = AlgorithmArray([1, 5, 8, 9, 10, 17, 17, 20, 24, 30])


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -INF
    for i in count(1, n):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-INF]*(n+1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -INF
        for i in count(1, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = [None]*(n+1)
    r[0] = 0
    # j is size of sub problem.
    for j in count(1, n):
        q = -INF
        for i in count(1, j):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n) -> Tuple:
    r = [None]*(n+1); s = [None]*(n+1)
    r[0] = 0
    for j in count(1, n):
        q = -INF
        for i in count(1, j):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def ext_memoized_cut_rod(p, n):
    r = [-INF]*(n+1)
    s = [None]*(n+1)
    return ext_memoized_cut_rod_aux(p, n, r, s)


def ext_memoized_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return r[n], s
    if n == 0:
        q = 0
    else:
        q = -INF
        for i in count(1, n):
            rec, _ = ext_memoized_cut_rod_aux(p, n - i, r, s)
            rec = p[i] + rec
            if q < rec:
                q = rec
                s[n] = i
    r[n] = q
    return q, s


def matrix_chain_order(p: List[int]):
    n = len(p) - 1
    m = AlgorithmArray.empty_n_m(n, n); s = AlgorithmArray.empty_n_m(n-1, n-1)
    for i in count(1, n):
        m[i][i] = 0
    for l in count(2, n):
        for i in count(1, n-l+1):
            j = i+l-1
            m[i][j] = INF
            for k in count(i, j-1):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j-1] = k
    return m, s


if __name__ == "__main__":
    p_table = [5, 10, 3, 12, 5, 50, 6]
    m, _ = matrix_chain_order(p_table)
    print(m[1][6])
    print(m)

