#!/usr/bin/env python
# coding=utf-8

# Inferring Protein from Spectrum
# ===============================
# 
# The prefix spectrum of a weighted string is the collection of all its prefix
# weights.
# 
# Given: A list L of n (n≤100) positive real numbers.
# 
# Return: A protein string of length n−1 whose prefix spectrum is equal to L (if
# multiple solutions exist, you may output any one of them). Consult the
# monoisotopic mass table.
# 
# Sample Dataset
# --------------
# 3524.8542
# 3710.9335
# 3841.974
# 3970.0326
# 4057.0646
# 
# Sample Output
# -------------
# WMQS


MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


def protein_string(s):
    result = ''
    prefix_spectrum = map(float, s.split())

    inverted_table = {}
    for k, v in MONOISOTOPIC_MASS_TABLE.iteritems():
        inverted_table[round(v, 4)] = k

    for i in range(1, len(prefix_spectrum)):
        a = prefix_spectrum[i - 1]
        b = prefix_spectrum[i]
        result += inverted_table[round(b - a, 4)]

    return result


if __name__ == "__main__":

    small_dataset = """
                    3524.8542
                    3710.9335
                    3841.974
                    3970.0326
                    4057.0646
                    """
    large_dataset = open('datasets/rosalind_spec.txt').read().strip()

    print protein_string(large_dataset)


