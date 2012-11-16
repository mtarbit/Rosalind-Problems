#!/usr/bin/env python
# coding=utf-8

# Inferring mRNA from Protein
# ===========================
# 
# For positive integers a and n, a modulo n (written amodn in shorthand) is the
# remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.
# 
# Modular arithmetic is the study of addition, subtraction, multiplication, and
# division with respect to the modulo operation. We say that a and b are
# congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.
# 
# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then
# a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you
# may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.
# 
# As you will see in this exercise, some Rosalind problems will ask for a (very
# large) integer solution modulo a smaller number to avoid the computational
# pitfalls that arise with storing such large numbers.
# 
# Given: A protein string of length at most 1000 aa.
# 
# Return: The total number of different RNA strings from which the protein could
# have been translated, modulo 1,000,000. (Don't neglect the importance of the
# stop codon in protein translation.)
# 
# Sample Dataset
# --------------
# MA
# 
# Sample Output
# -------------
# 12


RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def codon_frequencies():
    frequencies = {}
    for k, v in RNA_CODON_TABLE.iteritems():
        if not frequencies.has_key(v):
            frequencies[v] = 0
        frequencies[v] += 1
    return frequencies


def possible_rna_strings(input):
    f = codon_frequencies()
    n = f['Stop']

    for c in input:
        n *= f[c]

    return n


if __name__ == "__main__":

    small_dataset = "MA"
    large_dataset = open('datasets/rosalind_mrna.txt').read().strip()

    print possible_rna_strings(large_dataset) % 1000000

