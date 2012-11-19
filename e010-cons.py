#!/usr/bin/env python
# coding=utf-8

# Consensus and Profile
# =====================
# 
# A matrix is a rectangular table of values divided into rows and columns. An
# m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to
# indicate the value found at the intersection of row i and column j. You may
# choose to think of A as a collection of m arrays, each of length n.
# 
# Say that we have a collection of DNA strings, all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,j represents the number of
# times that 'A' occurs in the jth position of one of the strings, P2,j
# represents the number of times that C occurs in the jth position, and so on
# (see below).
# 
# A consensus string c is a string of length n formed from our collection by
# taking the most common symbol at each position; the jth symbol of c therefore
# corresponds to the symbol having the maximum value in the j-th column of the
# profile matrix. Of course, there may be more than one most common symbol,
# leading to multiple possible consensus strings.
# 
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp).
# 
# Return: A consensus string and profile matrix for the collection. (If several
# possible consensus strings exist, then you may return any one of them.)
# 
# Sample Dataset
# --------------
# ATCCAGCT
# GGGCAACT
# ATGGATCT
# AAGCAACC
# TTGGAACT
# ATGCCATT
# ATGGCACT
# 
# Sample Output
# -------------
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6


def profile(matrix):
    strings = matrix.split()

    default = [0] * len(strings[0])
    results = {
        'A': default[:],
        'C': default[:],
        'G': default[:],
        'T': default[:],
    }

    for s in strings:
        for i, c in enumerate(s):
            results[c][i] += 1

    return results


def consensus(profile):
    result = []

    keys = profile.keys()

    for i in range(len(profile[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = profile[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        result.append(max_k)

    return ''.join(result)


if __name__ == "__main__":

    small_dataset = """
                    ATCCAGCT
                    GGGCAACT
                    ATGGATCT
                    AAGCAACC
                    TTGGAACT
                    ATGCCATT
                    ATGGCACT
                    """

    large_dataset = open('datasets/rosalind_cons.txt').read()

    p = profile(large_dataset)
    c = consensus(p)

    print c
    for k in sorted(p.iterkeys()):
        print "%s: %s" % (k, ' '.join(map(str, p[k])))

