#!/usr/bin/env python
# coding=utf-8

# Introduction to Probability
# ===========================
# 
# Just as a string is an ordered collection of symbols, an array is an abstract
# structure ordering a collection of objects (numbers, strings, other arrays,
# etc.). A string could therefore be viewed as a specific case of array. We let
# A[k] denote the k-th value of A.
# 
# In a random string, each symbol is selected randomly from an alphabet based on
# some underlying distribution in which every symbol has a symbol frequency, or
# its own fixed chance of being drawn at any time.
# 
# GC-content gives us a natural way to form a realistic random DNA string for a
# given species. If the GC-content is x, then we make the symbol frequencies of
# C and G equal to x/2 and set the symbol frequencies of A and T equal to 1−x/2.
# In other words, if the GC-content is 40%, then as we construct the string, we
# have a 20% chance of the next added symbol being 'C', a 20% chance that it is
# 'G', a 30% chance that it is 'A', and a 30% chance that it is 'T'.
# 
# Given: An array A containing at most 20 real numbers between 0 and 1,
# inclusively.
# 
# Return: An array B in which B[i] represents the probability (to an accuracy of
# three decimal places) that for the GC-content in A[i], two randomly chosen
# symbols will be the same.
# 
# Sample Dataset
# --------------
# 0.23 0.31 0.75
# 
# Sample Output
# -------------
# 0.322900 0.286100 0.312500


def probabilities(s):
    results = []

    gc_contents = map(float, s.split())
    for x in gc_contents:
        a = x / 2.0
        b = (1 - x) / 2.0
        p = (a * a) + (a * a) + (b * b) + (b * b)
        results.append(p)

    return results


if __name__ == "__main__":

    small_dataset = "0.23 0.31 0.75"
    large_dataset = open('datasets/rosalind_prob.txt').read()

    results = probabilities(large_dataset)

    print ' '.join(map(str, results))

