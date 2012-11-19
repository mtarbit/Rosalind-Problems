#!/usr/bin/env python
# coding=utf-8

# Finding a Spliced Motif
# =======================
# 
# A subsequence of a string is a collection of symbols contained in order
# (though not necessarily contiguously) in the string (e.g., ACG is a
# subsequence of TATGCTAAGATC). The indices of a subsequence are the positions
# in the string at which the symbols of the subsequence appear; thus, the
# indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
# 
# As a substring can have multiple locations, a subsequence can have multiple
# collections of indices, and the same index can be reused in more than one
# appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT
# in 8 different ways.
# 
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# 
# Return: One collection of indices of s in which the symbols of t appear as a
# subsequence of s. If multiple solutions exist, you may return any one.
# 
# Sample Dataset
# --------------
# ACGTACGTGACG
# GTA
# 
# Sample Output
# -------------
# 3 8 10


def subsequence_indices(s):
    indices = []

    s, t = s.split()

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            indices.append(i + 1)
            j += 1
        i += 1

    return indices


if __name__ == "__main__":

    small_dataset = "ACGTACGTGACG\nGTA"
    large_dataset = open('datasets/rosalind_sseq.txt').read().strip()

    result = subsequence_indices(large_dataset)

    print ' '.join(map(str, result))


