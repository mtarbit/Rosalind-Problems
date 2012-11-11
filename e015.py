#!/usr/bin/env python
# coding=utf-8

# Enumerating k-mers Lexicographically
# ====================================
# 
# Assume that an alphabet 𝒜 has a predetermined order; that is, we write the
# alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the
# English alphabet is organized as (A,B,…,Z).
# 
# Given two strings s=s1s2⋯sn and t=t1t2⋯tn of the same length, we say that s
# precedes t in the lexicographic order (and write s<Lext) if the first symbol
# s[j] that doesn't match t[j] satisfies sj<tj in 𝒜.
# 
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a
# positive integer n (n≤10).
# 
# Return: All strings of length n that can be formed from the alphabet, ordered
# lexicographically.
# 
# Sample Dataset
# --------------
# T A G C
# 2
# 
# Sample Output
# -------------
# TT
# TA
# TG
# TC
# AT
# AA
# AG
# AC
# GT
# GA
# GG
# GC
# CT
# CA
# CG
# CC


def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


if __name__ == "__main__":

    small_dataset = "T A G C\n2"
    large_dataset = open('datasets/rosalind_lexf.txt').read()

    bits = large_dataset.split()

    alphabet = bits[:-1]
    comb_len = int(bits[-1])

    for p in alpha_combs(alphabet, comb_len):
        print p

