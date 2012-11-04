#!/usr/bin/env python
# coding=utf-8

# Finding a Motif in DNA
# ======================
# 
# Given two strings s = s1 s2 ... sn and t = t1 t2 ... tm where m ≤ n, t is a
# substring of s if t is contained as a contiguous collection of symbols in s.
# 
# The position of a symbol in a string is the total number of symbols found to
# its left, including itself (e.g., the positions of all occurrences of U in
# AUGCUUCAGAAAGGUCUUACG are 2, 5, 6, 15, 17, and 18). The symbol at position i
# of s is denoted by s[i]. For that matter, a substring of s can be represented
# as s[j:k], where j and k represent the starting and ending positions of the
# substring in s.
# 
# The location of a substring is its beginning position; note that t will have
# multiple locations in s if it occurs more than once as a substring of s (see
# the Sample sections below).
# 
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# 
# Return: All locations of t as a substring of s.
# 
# Sample Dataset
# --------------
# ACGTACGTACGTACGT
# GTA
# 
# Sample Output
# -------------
# 3 7 11


def locations(s_and_t):
    results = []

    s, t = s_and_t.split()
    l = len(t)

    for i in range(len(s) - l):
        if s[i:i+l] == t:
            results.append(i + 1)

    return results


if __name__ == "__main__":

    small_dataset = "ACGTACGTACGTACGT\nGTA"
    large_dataset = open('datasets/rosalind_subs.txt').read()

    results = locations(large_dataset)

    print ' '.join(map(str, results))

