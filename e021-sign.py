#!/usr/bin/env python
# coding=utf-8

# Enumerating Oriented Gene Orderings
# ===================================
# 
# A signed permutation of length n is some ordering of the positive integers
# {1,2,…,n} in which each integer is then provided with either a positive or
# negative sign (for the sake of simplicity, we omit the positive sign). For
# example, π=(5,−3,−2,1,4) is a signed permutation of length 5.
# 
# Given: A positive integer n≤6.
# 
# Return: The total number of signed permutations of length n, followed by a list
# of all such permutations (you may list the signed permutations in any order).
# 
# Sample Dataset
# --------------
# 2
# 
# Sample Output
# -------------
# 8
# -1 -2
# -1 2
# 1 -2
# 1 2
# -2 -1
# -2 1
# 2 -1
# 2 1


from itertools import permutations, product


def merge_product(product):
    result = []
    numbers, signs = product
    for i, number in enumerate(numbers):
        sign = signs[i]
        number = int(sign + str(number))
        result.append(number)
    return result


def result(n):
    numbers = list(permutations(range(1, n + 1)))
    signs = list(product('-+', repeat=n))

    results = list(product(numbers, signs))
    results = map(merge_product, results)

    return results


if __name__ == "__main__":

    small_dataset = 2
    large_dataset = int(open('datasets/rosalind_sign.txt').read().strip())

    results = result(large_dataset)

    print len(results)
    for r in results:
        print ' '.join(map(str, r))

