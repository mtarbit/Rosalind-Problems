#!/usr/bin/env python
# coding=utf-8

# Ordering Strings of Varying Length Lexicographically
# ====================================================
# 
# Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the
# substring t′=t[1:m]. We have two cases:
# 
# If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
# Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′
# (e.g., APPLET<LexARTS because APPL<LexARTS).  Given: A permutation of at most
# 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).
# 
# Return: All strings of length at most n formed from 𝒜, ordered
# lexicographically. (Note: As in “Enumerating k-mers Lexicographically”,
# alphabet order is based on the order in which the symbols are given.)
# 
# Sample Dataset
# --------------
# D N A
# 3
# 
# Sample Output
# -------------
# D
# DD
# DDD
# DDN
# DDA
# DN
# DND
# DNN
# DNA
# DA
# DAD
# DAN
# DAA
# N
# ND
# NDD
# NDN
# NDA
# NN
# NND
# NNN
# NNA
# NA
# NAD
# NAN
# NAA
# A
# AD
# ADD
# ADN
# ADA
# AN
# AND
# ANN
# ANA
# AA
# AAD
# AAN
# AAA


def alpha_combs(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


def result(s):
    bits = s.split()
    alphabet = bits[:-1]
    length = int(bits[-1])
    return alpha_combs(alphabet, length)


if __name__ == "__main__":

    small_dataset = "D N A\n3"
    large_dataset = open('datasets/rosalind_lexv.txt').read().strip()

    print "\n".join(result(large_dataset))


