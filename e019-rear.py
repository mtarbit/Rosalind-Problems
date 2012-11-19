#!/usr/bin/env python
# coding=utf-8

# Reversal Distance
# =================
# 
# A reversal of a permutation creates a new permutation by inverting some
# interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all
# reversals of (5,3,2,1,4). The reversal distance between two permutations π and
# σ, written drev(π,σ), is the minimum number of reversals required to transform
# π into σ (this assumes that π and σ have the same length).
# 
# Given: A collection of at most 5 pairs of permutations, all of which have
# length 10.
# 
# Return: The reversal distance between each permutation pair.
# 
# Sample Dataset
# --------------
# 1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8
# 
# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9
# 
# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4
# 
# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10
# 
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 
# Sample Output
# -------------
# 9 4 5 7 0


def handle_pair(pair):
    lines = pair.split("\n")
    lines = [map(int, l.split()) for l in lines]
    return lines


# See the section on inverse permutations and sorting by reversals here:
# http://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1103&context=etd_projects


def inverse_permutation(a):
    p = [None] * len(a)
    for i, n in enumerate(a):
        p[n - 1] = i + 1 
    return p


def apply_permutation(p, b):
    t = []
    for n in b:
        t.append(p[n - 1])
    return t


def reversal_distance(a, b):
    p = inverse_permutation(b)
    a = apply_permutation(p, a)
    l = len(a)
    r = 0

    print '-' * 24

    for j in range(l, 1, -1):
        for i in range(l):
            if a[i] == j:
                break
        if (j - i) > 1:
            print ' '.join([str(0 if x == 10 else x) for x in a]), ':', j
            print ' '.join(([' '] * i) + (['-'] * (j - i)))
            a[i:j] = reversed(a[i:j])
            r += 1

    print r



def result(s):
    pairs = s.strip().split("\n\n")
    pairs = [handle_pair(p) for p in pairs]

    for a, b in pairs:
        reversal_distance(a, b)


if __name__ == "__main__":

    small_dataset = """
                    1 2 3 4 5 6 7 8 9 10
                    3 1 5 2 7 4 9 6 10 8

                    3 10 8 2 5 4 7 1 6 9
                    5 2 3 1 7 4 10 8 6 9

                    8 6 7 9 4 1 3 10 2 5
                    8 2 7 6 9 1 5 3 10 4

                    3 9 10 4 1 8 6 7 5 2
                    2 9 8 5 1 7 3 4 6 10

                    1 2 3 4 5 6 7 8 9 10
                    1 2 3 4 5 6 7 8 9 10
                    """
    # large_dataset = open('datasets/rosalind_rear.txt').read().strip()

    result(small_dataset)

