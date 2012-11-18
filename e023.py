#!/usr/bin/env python
# coding=utf-8

# k-Mer Composition
# =================
# 
# For a fixed positive integer k, order all possible k-mers taken from an
# underlying alphabet lexicographically.
# 
# Then the k-mer composition of a string s can be represented by an array A for
# which A[m] denotes the number of times that the mth k-mer (with respect to the
# lexicographic order) appears in s.
# 
# Given: A DNA string s in FASTA format (having length at most 100 kbp).
# 
# Return: The 4-mer composition of s.
# 
# Sample Dataset
# --------------
# >Rosalind_6431
# CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
# CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
# TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
# AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
# GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
# CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
# CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
# 
# Sample Output
# -------------
# 4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1


from itertools import product


def parse_fasta(fasta):
    results = []
    strings = fasta.strip().split('>')

    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append((k, v))

    return results


def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]


def kmer_composition(s, k):
    kmers = {}
    
    for kmer in possible_kmers(k):
        kmers[kmer] = 0

    for i in range(len(s) - (k - 1)):
        kmer = s[i:i+k]
        kmers[kmer] += 1

    return kmers


def result(s):
    fastas = parse_fasta(s)
    k_comp = kmer_composition(fastas[0][1], 4)

    result = []
    for kmer in sorted(k_comp.iterkeys()):
        result.append(k_comp[kmer])
        
    return result


if __name__ == "__main__":

    small_dataset = """
                    >Rosalind_6431
                    CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
                    CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
                    TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
                    AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
                    GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
                    CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
                    CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
                    """
    large_dataset = open('datasets/rosalind_kmer.txt').read().strip()

    print ' '.join(map(str, result(large_dataset)))


