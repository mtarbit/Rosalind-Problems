#!/usr/bin/env python

# Counting Point Mutations
# ========================
# 
# Given two strings s and t of equal length, the Hamming distance between s and 
# t, denoted dH(s,t), is the number of corresponding symbols that differ in s 
# and t. See Figure 2.
# 
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# 
# Return: The Hamming distance dH(s,t).
# 
# Sample Dataset
# --------------
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# 
# Sample Output
# -------------
# 7


def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1
 
    return dh


if __name__ == "__main__":

    small_dataset = """
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    """

    large_dataset = open('datasets/rosalind_hamm.txt').read()

    s, t = large_dataset.split()
    dist = hamming_distance(s, t)

    print dist

