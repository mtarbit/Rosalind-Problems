#!/usr/bin/env python
# coding=utf-8

# Genome Assembly as Shortest Superstring
# =======================================
# 
# Given a collection of strings, a larger string containing every one of the
# smaller strings as a substring is called a superstring.
# 
# By the assumption of parsimony, a shortest possible superstring over a
# collection of reads serves as a candidate chromosome.
# 
# Given: At most 50 DNA strings of equal length not exceeding 1 kbp (which
# represent reads deriving from the same strand of a single linear chromosome).
# 
# The dataset is guaranteed to satisfy the following condition: there exists a
# unique way to reconstruct the entire chromosome from these reads by gluing
# together pairs of reads that overlap by more than half their length.
# 
# Return: A shortest superstring containing all the given strings (thus
# corresponding to a reconstructed chromosome).
# 
# Sample Dataset
# --------------
# ATTAGACCTG
# CCTGCCGGAA
# AGACCTGCCG
# GCCGGAATAC
# 
# Sample Output
# -------------
# ATTAGACCTGCCGGAATAC


def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])


if __name__ == "__main__":

    small_dataset = """
                    ATTAGACCTG
                    CCTGCCGGAA
                    AGACCTGCCG
                    GCCGGAATAC
                    """
    large_dataset = open('datasets/rosalind_long.txt').read().strip()

    print find_overlaps(large_dataset.split())


