#!/usr/bin/env python

# GC Content
# ==========
# 
# DNA strings must be labeled when they are consolidated into a database. A 
# commonly used method of string labeling is called FASTA format. In this 
# format, the string is introduced by a line that begins with ">", followed by 
# some information naming and characterizing the string. Subsequent lines 
# contain the string itself; the next line starting with ">" indicates the label
# of the next string.
# 
# In Rosalind's implementation, a string in FASTA format will be labeled by the 
# ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 
# 9999.
# 
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest GC-content, followed by the 
# GC-content of that string. The GC-content should have an accuracy of 4 decimal 
# places (see the note below on decimal accuracy).
# 
# Sample Dataset
# --------------
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# 
# Sample Output
# -------------
# Rosalind_0808
# 60.919540%


def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results[label] = bases
        
    return results


def gc_content(s):
    n = len(s)
    m = 0

    for c in s:
        if c == 'G' or c == 'C':
            m += 1

    return 100 * (float(m) / n)


if __name__ == "__main__":

    small_dataset = """
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
    """

    large_dataset = open('datasets/rosalind_gc.txt').read()

    results = parse_fasta(large_dataset)
    results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

    highest_k = None
    highest_v = 0

    for k, v in results.iteritems():
        if v > highest_v:
            highest_k = k
            highest_v = v

    print highest_k
    print '%f%%' % highest_v

