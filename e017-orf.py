#!/usr/bin/env python
# coding=utf-8

# Open Reading Frames
# ===================
# 
# Either strand of a DNA double helix can serve as the coding strand for RNA
# transcription. Hence, a given DNA string implies six total reading frames, or
# ways in which the same region of DNA can be translated into amino acids: three
# reading frames result from reading the string itself, whereas three more
# result from reading its reverse complement.
# 
# An open reading frame (ORF) is one which starts from the start codon and ends
# by stop codon, without any other stop codons in between. Thus, a candidate
# protein string is derived by translating an open reading frame into amino
# acids until a stop codon is reached.
# 
# Given: A DNA string s of length at most 1 kbp.
# 
# Return: Every distinct candidate protein string that can be translated from
# ORFs of s. Strings can be returned in any order.
# 
# Sample Dataset
# --------------
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# 
# Sample Output
# -------------
# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
# MTPRLGLESLLE


DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def translate_codon(codon):
    protein = None
    if len(codon) == 3 and DNA_CODON_TABLE.has_key(codon):
        protein = DNA_CODON_TABLE[codon]
    return protein


def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results


if __name__ == "__main__":

    small_dataset = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    large_dataset = open('datasets/rosalind_orf.txt').read().strip()

    possible_a = possible_protein_strings(large_dataset)
    possible_b = possible_protein_strings(reverse_complement(large_dataset))
    print "\n".join(set(possible_a + possible_b))

