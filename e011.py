#!/usr/bin/env python
# coding=utf-8

# Introduction to Expected Value
# ==============================
# 
# Given a finite collection of events x1,x2,…,xn, where xi has probability pi,
# the expected value for the number of events occurring is given by p1+p2+⋯+pn.
# 
# As a simple example, if you were to place 4 bets on sporting events this
# weekend, and the probability of each of your bets winning is 0.4, 0.7, 0.8,
# and 0.5, then the expected value for the number of bets you will win is 0.4 +
# 0.7 + 0.8 + 0.5 = 2.4. Notice that this value is a decimal even though you can
# only win a whole number of your bets, and also that the expected value only
# quantifies an average case scenario: it says nothing about the actual outcome
# of your gambling habit.
# 
# Given: A positive integer m (m≤10), a positive integer n (n≤10,000), and an
# array A of length at most 20 containing real numbers between 0 and 1,
# inclusively.
# 
# Return: An array B in which B[i] represents the expected number of substring
# matches of a random string of length m inside a random string of length n,
# where both are formed from GC-content A[i] (see “Introduction to
# Probability”). Each value in B should be accurate to three decimal places.
# 
# Sample Dataset
# --------------
# 2 10
# 0.32 0.42 0.81
# 
# Sample Output
# -------------
# 0.717748 0.591669 1.078067


from math import pow


def symbol_match_probability(gc):
    a = gc / 2.0
    b = (1 - gc) / 2.0
    p = (a * a) + (a * a) + (b * b) + (b * b)
    return p


def string_match_probability(gc, l):
    return pow(symbol_match_probability(gc), l)


def expected_matches(m, n, gc):
    positions = 1 + (n - m)
    probability = string_match_probability(gc, m)
    return positions * probability


def calculate_expected(input):
    bits = input.split()

    m = int(bits[0])
    n = int(bits[1])
    gc_contents = map(float, bits[2:])

    return [expected_matches(m, n, gc) for gc in gc_contents]


if __name__ == "__main__":
    small_dataset = "2 10\n0.32 0.42 0.81"
    large_dataset = open('datasets/rosalind_eval.txt').read()

    results = calculate_expected(large_dataset)

    print ' '.join(map(str, results))

