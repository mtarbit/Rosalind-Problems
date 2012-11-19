#!/usr/bin/env python

# Reverse Complement
# ==================
# 
# In a DNA string, the complement of A is T, and the complement of C is G.
# 
# The reverse complement of a DNA string s is the string sc formed by reversing 
# the symbols of s, then taking the complement of each symbol (e.g., the reverse
# complement of GTCA is TGAC).
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: The reverse complement of s.
# 
# Sample Dataset
# --------------
# AAAACCCGGT
# 
# Sample Output
# -------------
# ACCGGGTTTT


def reverse_complement(s):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    
    sc = reversed(s)
    sc = [complements[c] for c in sc]

    return ''.join(sc)


if __name__ == "__main__":

    small_dataset = "AAAACCCGGT"
    large_dataset = "GGTTGTCTTCACGACAACACCGCGCTGGCCAAGGTATTAAATAGGCGCATCACTGCTTCTCCCATGACATTGAAAAGGTTAACTTCCCCCATCCAACGTCAGTCTCCATTCTTTCAGTCGGGGGCAAATATGACCGGAGTTAAAGGACTCGAGCTATTGCAGAGCCACGGACGAGAGCAATTCACCAGAGCATAGCAAAAGTGCCGGCCGGCCTACGACCCGGAGACCGTGAAGTTGCGTCCCATTGCTGTTGCATTACAACCGCTCGCGAACGCATCAGTTGGTATATATATCTAAAAGCGTGGCGTGGCCTTGGTACTATTCGGAGAGATCCTAGTTATGCATGAGCAAGCTCGCCGTACGGGTCTGCCACGGTGGAGTTGAGTTTGTAGGCGATAGCCTAGCCGACGGGCTGACTGCGCCAAGAGACTTTCTCCTGATTGAGCTTATGATTGAAAGGCAACGACACAATCATATCGCCGGCGAGTAGACGTCTACTAAAGTTACAGTATTATTTAGCGGCTGAGGAGTTCACACCCTGTCCCAGGTGCGGACAATACTGCTATCTAGGGGCACATGGGTGATGGCATCGGACCGTATTGGATGGGAGGAAATTGGTTCCTTTAGACTAAAGGGTCGTTTCAGCGACAAATATTCAACGTCCCTCTTTTCGGATTTCATTTGCTCATGCAGATCGTGACTACTTACCTGCGACCCGGTAGACATGTGAAGGCTGTTTGTCTAATATCCTTGCATGAGGGTCGACGTATATTGGTCTACCAGGTTCAAGACAGCGGACTATGTATAATCTTCTGGTGTTCCATTAACTCACCCTCAGACCCGACGAAATCCAGCCAACCCTGGGAACTGATATCCCCACAAAATTTCTC"

    print reverse_complement(large_dataset)
