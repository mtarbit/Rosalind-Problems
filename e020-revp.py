#!/usr/bin/env python
# coding=utf-8

# Locating Restriction Sites
# ==========================
# 
# A DNA string is a reverse palindrome if it is equal to its reverse complement.
# For instance, GCATGC is a reverse palindrome because its reverse complement is
# GCATGC.
# 
# Given: A DNA string of length at most 1 kbp.
# 
# Return: The position and length of every reverse palindrome in the string
# having length between 4 and 8.
# 
# Sample Dataset
# --------------
# TCAATGCATGCGGGTCTATATGCAT
# 
# Sample Output
# -------------
# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4


def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([complements[c] for c in reversed(s)])


def reverse_palindromes(s):
    results = []

    l = len(s)

    for i in range(l):
        for j in range(4, 9):

            if i + j > l:
                continue

            s1 = s[i:i+j]
            s2 = reverse_complement(s1)

            if s1 == s2:
                results.append((i + 1, j))

    return results


if __name__ == "__main__":

    small_dataset = "TCAATGCATGCGGGTCTATATGCAT"
    large_dataset = open('datasets/rosalind_revp.txt').read().strip()

    results = reverse_palindromes(large_dataset)

    print "\n".join([' '.join(map(str, r)) for r in results])

