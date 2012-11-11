#!/usr/bin/env python
# coding=utf-8

# Finding a Shared Motif
# ======================
# 
# A common substring of a collection of strings is a substring of every member
# of the collection. We say that a common substring is a longest common
# substring if a longer common substring of the collection does not exist. For
# example, CG is a common substring of ACGTACGT and AACCGGTATA, whereas GTA is a
# longest common substring. Note that multiple longest common substrings may
# exist.
# 
# Given: A collection of k DNA strings (of length at most 1 kbp each; k≤100).
# 
# Return: A longest common substring of the collection. (If multiple solutions
#         exist, you may return any single solution.)
# 
# Sample Dataset
# --------------
# GATTACA
# TAGACCA
# ATACA
# 
# Sample Output
# -------------
# AC


def lcs(strings):
    result = ''

    strings = sorted(strings.split())
    short_string = strings[0]
    other_strings = strings[1:]

    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break

    return m


if __name__ == "__main__":

    small_dataset = "GATTACA\nTAGACCA\nATACA"
    large_dataset = open('datasets/rosalind_lcs.txt').read()

    print lcs(large_dataset)

