#!/usr/bin/env python
# coding=utf-8

# Speeding Up Motif Finding
# =========================
# 
# A prefix of a string s having length n is a substring s[1:j]; a suffix of s is
# a substring s[k:n].
# 
# The failure array of s is an array P of length n for which P[k] is the length
# of the longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where
# j cannot equal 1 (otherwise, P[k] would always equal k). By convention,
# P[1]=0.
# 
# Given: A DNA string s (of length at most 100 kbp).
# 
# Return: The failure array of s.
# 
# Sample Dataset
# --------------
# CAGTAAGCAGGGACTG
# 
# Sample Output
# -------------
# 0 0 0 0 0 0 0 1 2 3 0 0 0 1 0 0


def kmp_preprocess(s):
    j = -1
    b = [j]

    for i, c in enumerate(s):
        while j >= 0 and s[j] != c:
            j = b[j]
        j += 1
        b.append(j)

    return b[1:]


if __name__ == "__main__":

    small_dataset = "CAGTAAGCAGGGACTG"
    large_dataset = open('datasets/rosalind_kmp.txt').read()

    results = kmp_preprocess(large_dataset)

    print ' '.join(map(str, results))

