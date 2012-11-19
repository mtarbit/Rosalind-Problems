#!/usr/bin/env python
# coding=utf-8

# Enumerating Gene Orders
# =======================
# 
# A permutation of length n is some ordering of the positive integers {1,2,…,n}. 
# For example, π=(5,3,2,1,4) is a permutation of length 5.
# 
# Given: A positive integer n≤7.
# 
# Return: The total number of permutations of length n, followed by a list of 
# all such permutations (in any order).
# 
# Sample Dataset
# --------------
# 3
# 
# Sample Output
# -------------
# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1


def fac(n):
    if n <= 2:
        return n
    else:
        return n * fac(n-1)


def permutations(n):
    a = range(1, n+1)

    while True:
        yield a[:]

        k = l = None

        for i in range(0, len(a) - 1):
            if a[i] < a[i+1]:
                k = i

        if k == None:
            break

        for i in range(k + 1, len(a)):
            if a[k] < a[i]:
                l = i

        a[k], a[l] = a[l], a[k]
        a[k+1:] = reversed(a[k+1:])


if __name__ == "__main__":

    small_dataset = 3
    large_dataset = 7

    n = large_dataset

    print fac(n)
    for p in permutations(n):
        print ' '.join(map(str, p))

