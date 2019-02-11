#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""

import numpy as np

# def main():
#     """
#     Main function documentation template
#     :return: None
#     :rtype: None
#     """
#     logging.getLogger().setLevel(logging.INFO)
# 
#     # Extract data from upstream.
#     observations = extract()
# 
#     # Spacy: Spacy NLP
#     nlp = spacy.load('en')
# 
#     # Transform data to have appropriate fields
#     observations, nlp = transform(observations, nlp)
# 
#     # Load data for downstream consumption
#     load(observations, nlp)
# 
#     pass




def sieve_eratosthenes(n):
    primes = [False, False] + [True for i in range(n-1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    return np.array(primes).astype(int)

# Main section
if __name__ == '__main__':
    main()
